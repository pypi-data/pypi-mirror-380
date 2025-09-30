#!/usr/bin/env python
"""
PDG Universal Wrapper Script for Conductor Render Farm
Supports three modes:
- Submit As Job (full graph execution)
- On Schedule (single work item execution)
- Single Machine (cook all items locally)
"""

import hou
import os
import sys
import argparse
import time
import random
import json
import shutil
import glob
import re
import traceback
from pathlib import Path
from datetime import datetime
import subprocess


class PDGUniversalExecutor:
    """Universal executor for submitAsJob, on_schedule, and single_machine modes"""

    def __init__(self, hip_file, topnet_path, working_dir, output_dir,
                 item_index=None, cook_entire_graph=False, use_single_machine=False):
        self.hip_file = hip_file
        self.topnet_path = topnet_path
        self.working_dir = working_dir
        self.output_dir = output_dir


        self.output_dir = self.clean_path(self.output_dir)

        # Execution mode - set this BEFORE initializing status dict
        """
        self.item_index = item_index
        self.cook_entire_graph = cook_entire_graph
        self.use_single_machine = use_single_machine
        if cook_entire_graph:
            self.execution_mode = "submitAsJob"
        elif use_single_machine:
            self.execution_mode = "single_machine"
        else:
            self.execution_mode = "on_schedule"
        """
        self.item_index = item_index
        self.cook_entire_graph = False
        self.use_single_machine = True
        self.execution_mode = "single_machine"

        # Initialize status dict after execution_mode is set
        self.status_dict = self._initialize_status_dict()

        # Initialize other attributes
        self.topnet = None
        self.scheduler = None
        self.output_node = None

    def _initialize_status_dict(self):
        """Initialize the status tracking dictionary"""
        # First part: basic fields
        base_dict = {
            'timestamp_start': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'execution_mode': self.execution_mode,
            'hip_file': self.hip_file,
            'topnet_path': self.topnet_path,
            'working_dir': self.working_dir,
            'output_dir': self.output_dir,
        }


        # Second part: Add mode-specific fields
        if self.cook_entire_graph:
            base_dict['cook_entire_graph'] = True
            base_dict['work_items_total'] = 0
            base_dict['work_items_succeeded'] = 0
            base_dict['work_items_failed'] = 0
            base_dict['work_items_details'] = []
        elif self.use_single_machine:
            base_dict['use_single_machine'] = True
            base_dict['work_items_total'] = 0
            base_dict['work_items_succeeded'] = 0
            base_dict['work_items_failed'] = 0
            base_dict['work_items_details'] = []
        else:
            base_dict['target_index'] = self.item_index
            base_dict['frame_number'] = str(self.item_index).zfill(4) if self.item_index is not None else "0000"
            base_dict['work_items_processed'] = []
            base_dict['skipped_items'] = []

        # Third part: remaining fields
        base_dict.update({
            'nodes_in_network': [],
            'files_created': {
                'usd': [],
                'renders': [],
                'hip': [],
                'logs': [],
                'pdg': [],
                'geo': [],
                'other': [],
                'wedge_outputs': [],
                'total_count': 0
            },
            'cook_result': {
                'return_code': None,
                'failed_items': [],
                'successful_items': [],
                'warnings': []
            },
            'environment': dict(os.environ),
            'timestamp_end': None,
            'duration_seconds': None,
            'status': 'initializing',
            'errors': []
        })

        return base_dict

    def run(self):
        """Main execution method"""
        try:
            print("\n" + "=" * 80)
            print("PDG UNIVERSAL WRAPPER SCRIPT")
            print(f"EXECUTION MODE: {self.execution_mode.upper()}")
            print("=" * 80)
            self._print_configuration()

            # Phase 1: Setup
            if not self._setup_environment():
                return False

            # Phase 2: Load HIP file
            if not self._load_hip_file():
                return False

            # Phase 3: Get TOP Network
            if not self._get_top_network():
                return False

            # Execute based on mode
            if self.cook_entire_graph:
                # Submit As Job mode - cook entire graph
                # Phase 4: Create and configure scheduler for full graph
                if not self._setup_scheduler_for_full_graph():
                    return False
                # Phase 5: Execute full graph
                success = self._execute_full_graph()
            elif self.use_single_machine:
                # Single Machine mode - cook all items locally
                # Phase 4: Create scheduler (no custom code needed)
                if not self._setup_scheduler_for_single_machine():
                    return False
                # Phase 5: Execute all work items locally
                success = self._execute_single_machine()
            else:
                # On Schedule mode - cook single work item
                # Phase 4: Create and configure scheduler
                if not self._setup_scheduler():
                    return False
                # Phase 5: Generate and cook work items
                success = self._execute_work_items()

            # Phase 6: Collect all output files
            self._collect_all_outputs()

            # Phase 7: Save final HIP file
            self._save_final_hip()

            self.status_dict['status'] = 'success' if success else 'failure'
            return success

        except Exception as e:
            self.status_dict['errors'].append(str(e))
            self.status_dict['status'] = 'error'
            print(f"\nCRITICAL ERROR: {e}")
            traceback.print_exc()
            return False

        finally:
            self._finalize_execution()

    def _print_configuration(self):
        """Print execution configuration"""
        print(f"HIP File: {self.hip_file}")
        print(f"TOP Network: {self.topnet_path}")
        print(f"Working Dir: {self.working_dir}")
        print(f"Output Dir: {self.output_dir}")

        if self.cook_entire_graph:
            print(f"Mode: Submit As Job (Full Graph Execution)")
        elif self.use_single_machine:
            print(f"Mode: Single Machine (Cook All Items Locally)")
        else:
            frame_num = str(self.item_index).zfill(4) if self.item_index is not None else "0000"
            print(f"Mode: On Schedule (Single Work Item)")
            print(f"Target Index: {self.item_index} (Frame: {frame_num})")

        print("=" * 80 + "\n")

    def _setup_environment(self):
        """Setup execution environment"""
        print("\n" + "-" * 60)
        print("Phase 1: Environment Setup")
        print("-" * 60)

        try:
            # Create output directory
            os.makedirs(self.output_dir, exist_ok=True)

            # Test write permissions
            test_file = os.path.join(self.output_dir, '.write_test')
            with open(test_file, 'w') as f:
                f.write('test')
            os.remove(test_file)
            print(f"✓ Output directory ready: {self.output_dir}")

            # Set PDG environment variables
            os.environ['PDG_DIR'] = self.working_dir
            os.environ['PDG_RENDER_DIR'] = self.output_dir

            # Create necessary subdirectories
            subdirs = ['usd', 'renders', 'logs', 'pdg', 'hip', 'execution_status']
            for subdir in subdirs:
                os.makedirs(os.path.join(self.output_dir, subdir), exist_ok=True)

            print("✓ Environment configured successfully")
            return True

        except Exception as e:
            print(f"✗ Environment setup failed: {e}")
            self.status_dict['errors'].append(f"Environment setup: {e}")
            return False

    def _load_hip_file(self):
        """Load the Houdini HIP file"""
        print("\n" + "-" * 60)
        print("Phase 2: Loading HIP File")
        print("-" * 60)

        try:
            if not os.path.exists(self.hip_file):
                raise FileNotFoundError(f"HIP file not found: {self.hip_file}")

            print(f"Loading: {self.hip_file}")

            # Load the file and capture any warnings
            try:
                hou.hipFile.load(self.hip_file, suppress_save_prompt=True, ignore_load_warnings=True)
            except hou.LoadWarning as warning:
                # This is just a warning, not an error - file loaded successfully
                print(f"  Note: Load warning (can be ignored): {warning}")
            except hou.OperationFailed as e:
                # This is an actual error
                if "Warnings were generated" in str(e):
                    # This is actually just warnings, not a failure
                    print(f"  Note: Warnings during load (continuing): {e}")
                else:
                    # This is a real failure
                    raise e

            # Verify load by checking the current file
            current_hip = hou.hipFile.name()
            if os.path.abspath(current_hip) == os.path.abspath(self.hip_file):
                print(f"✓ HIP file loaded successfully: {current_hip}")
            else:
                # Sometimes the path format differs, check if it's essentially the same file
                print(f"✓ HIP file loaded: {current_hip}")

            # Update paths if needed
            hou.hscript(f"set PDG_DIR = {self.working_dir}")
            hou.hscript(f"set PDG_RENDER_DIR = {self.output_dir}")

            return True

        except FileNotFoundError as e:
            print(f"✗ File not found: {e}")
            self.status_dict['errors'].append(f"HIP file not found: {e}")
            return False
        except Exception as e:
            # Check if this is just a warning about incomplete asset definitions
            error_str = str(e)
            if "Warnings were generated" in error_str or "incomplete asset definitions" in error_str:
                print(f"  Note: Load completed with warnings (continuing):")
                print(f"    {error_str}")

                # Verify the file actually loaded
                try:
                    current_hip = hou.hipFile.name()
                    print(f"✓ HIP file loaded despite warnings: {current_hip}")

                    # Update paths
                    hou.hscript(f"set PDG_DIR = {self.working_dir}")
                    hou.hscript(f"set PDG_RENDER_DIR = {self.output_dir}")

                    return True
                except:
                    # If we can't get the hip file name, it didn't load
                    print(f"✗ Failed to verify HIP file load")
                    self.status_dict['errors'].append(f"HIP load verification failed: {e}")
                    return False
            else:
                # This is a real error
                print(f"✗ Failed to load HIP file: {e}")
                self.status_dict['errors'].append(f"HIP load: {e}")
                return False

    def _get_top_network(self):
        """Find and validate TOP network"""
        print("\n" + "-" * 60)
        print("Phase 3: Locating TOP Network")
        print("-" * 60)

        # Try specified path first
        current_node = hou.node(self.topnet_path)

        if current_node:
            # Check if the node exists and find the topnet
            print(f"Node found at {self.topnet_path} (type: {current_node.type().name()})")
            print(f"  Category: {current_node.type().category().name()}")

            # Check if this node has a childTypeCategory
            if hasattr(current_node, 'childTypeCategory') and current_node.childTypeCategory():
                print(f"  Child category: {current_node.childTypeCategory().name()}")
            else:
                print(f"  Child category: None")

            # Check if this is a TOP network container (can contain TOP nodes)
            # TOP network containers have childTypeCategory of "Top"
            is_topnet_container = (hasattr(current_node, 'childTypeCategory') and
                                   current_node.childTypeCategory() and
                                   current_node.childTypeCategory().name() == "Top")

            if is_topnet_container:
                # It's already a TOP network container
                self.topnet = current_node
                self.topnet_path = current_node.path()
                print(f"✓ Node is a TOP network container: {self.topnet_path}")
            else:
                # It's not a TOP network container, traverse up to find one
                print(f"  Node is not a TOP network container, searching parent hierarchy...")

                # Start from current node's parent
                parent_node = current_node.parent() if current_node else None

                while parent_node is not None:
                    print(f"  Checking parent: {parent_node.path()}")

                    # Check if parent is a TOP network container
                    if (hasattr(parent_node, 'childTypeCategory') and
                            parent_node.childTypeCategory() and
                            parent_node.childTypeCategory().name() == "Top"):
                        self.topnet = parent_node
                        self.topnet_path = parent_node.path()
                        print(f"✓ Found TOP network container in parent: {self.topnet_path}")
                        break

                    # Move up to next parent
                    parent_node = parent_node.parent()

                # If we didn't find a topnet in the parent hierarchy
                if not self.topnet:
                    print(f"✗ No TOP network container found in parent hierarchy of {self.topnet_path}")
                    print("  Falling back to scene-wide search...")
                    self._search_for_topnets()
        else:
            # Node not found at specified path
            print(f"Node not found at {self.topnet_path}")
            print("  Falling back to scene-wide search...")
            self._search_for_topnets()

        # Final check - did we find a TOP network?
        if not self.topnet:
            print("✗ No TOP networks found in scene")
            self.status_dict['errors'].append("No TOP network found")
            return False

        print(f"\n✓ Using TOP network: {self.topnet_path}")
        print(f"  Type: {self.topnet.type().name()}")
        print(f"  Category: {self.topnet.type().category().name()}")
        if hasattr(self.topnet, 'childTypeCategory') and self.topnet.childTypeCategory():
            print(f"  Child category: {self.topnet.childTypeCategory().name()}")

        # Catalog nodes in network
        self._catalog_top_nodes()

        # Find output node
        self._find_output_node()

        return True

    def _search_for_topnets(self):
        """Search for TOP networks in the scene"""
        print("Searching for TOP networks...")

        top_networks = []

        # Search in /obj
        if hou.node("/obj"):
            for node in hou.node("/obj").children():
                if node.type().name() == "topnet":
                    top_networks.append(node)
                    print(f"  Found: {node.path()}")

        # Search in /tasks (common location for tasks)
        if hou.node("/tasks"):
            for node in hou.node("/tasks").children():
                if node.type().name() == "topnet":
                    top_networks.append(node)
                    print(f"  Found: {node.path()}")

        # Search everywhere else
        for root in ["/", "/stage"]:
            if hou.node(root):
                for child in hou.node(root).children():
                    if child.path() not in ["/obj", "/tasks"] and child.type().category():
                        for node in child.allSubChildren():
                            if node.type().name() == "topnet" and node not in top_networks:
                                top_networks.append(node)
                                print(f"  Found: {node.path()}")

        if top_networks:
            self.topnet = top_networks[0]
            self.topnet_path = self.topnet.path()
            print(f"✓ Using TOP network: {self.topnet_path}")
        else:
            self.topnet = None

    def _is_output_node(self, node):
        """Check if a node is an output-type node

        Args:
            node: A Houdini TOP node to check

        Returns:
            bool: True if this is an output-type node, False otherwise
        """
        output_types = ['output', 'ropfetch', 'ropgeometry', 'ropmantra',
                        'ropkarma', 'usdrender', 'filecopy', 'null', 'rop']
        node_type_lower = node.type().name().lower()

        for out_type in output_types:
            if out_type in node_type_lower:
                return True
        return False

    def _catalog_top_nodes(self):
        """Catalog all TOP nodes in the network"""
        print("\nCataloging TOP nodes:")
        for node in self.topnet.children():
            if node.type().category().name() == "Top":
                # Check display flag
                is_display = False
                try:
                    is_display = (self.topnet.displayNode() == node)
                except:
                    try:
                        is_display = node.isDisplayFlagSet()
                    except:
                        pass

                # Check render flag
                is_render = False
                try:
                    is_render = node.isRenderFlagSet()
                except:
                    # Some nodes don't have render flags
                    pass

                node_info = {
                    'path': node.path(),
                    'type': node.type().name(),
                    'display_flag': is_display,
                    'render_flag': is_render
                }
                self.status_dict['nodes_in_network'].append(node_info)

                flags = []
                if self._is_output_node(node):
                    flags.append("OUTPUT")
                if is_display:
                    flags.append("DISPLAY")
                if is_render:
                    flags.append("RENDER")

                flag_str = f" [{', '.join(flags)}]" if flags else ""
                print(f"  - {node.name()} ({node.type().name()}){flag_str}")

    def _find_output_node(self):
        """Find the appropriate output node"""
        print("\nIdentifying output node:")

        # Priority 1: Display node
        self.output_node = self.topnet.displayNode()
        if self.output_node:
            print(f"✓ Using display node: {self.output_node.name()}")
            return

        # Priority 2: Common output node types
        output_types = ['output', 'ropfetch', 'ropgeometry', 'ropmantra',
                        'ropkarma', 'usdrender', 'filecopy', 'null']

        for node in self.topnet.children():
            if node.type().category().name() == "Top":
                for out_type in output_types:
                    if out_type in node.type().name().lower():
                        self.output_node = node
                        print(f"✓ Using output node: {node.name()} ({node.type().name()})")
                        return

        # Priority 3: Last non-scheduler node
        top_nodes = [n for n in self.topnet.children()
                     if n.type().category().name() == "Top"
                     and "scheduler" not in n.type().name().lower()]

        if top_nodes:
            self.output_node = top_nodes[-1]
            print(f"✓ Using last TOP node: {self.output_node.name()}")
        else:
            print("✗ No suitable output node found")

    def _find_or_create_scheduler(self, preferred_types=None, custom_code=None):
        """
        Find an existing scheduler or create a new one with fallback strategies.

        Args:
            preferred_types: List of preferred scheduler types (e.g., ['pythonscheduler', 'localscheduler'])
            custom_code: Custom onSchedule code to set if modifying a Python scheduler

        Returns:
            The scheduler node if successful, None otherwise
        """
        if preferred_types is None:
            preferred_types = ['conductorscheduler', 'pythonscheduler', 'localscheduler']

        scheduler = None
        created_new = False

        print("\nScheduler acquisition strategy:")

        # Strategy 1: Try to create a new Python scheduler
        try:
            existing = self.topnet.node("temp_python_scheduler")
            if existing:
                existing.destroy()
                print("  Removed existing temp scheduler")

            scheduler = self.topnet.createNode('pythonscheduler', 'temp_python_scheduler')
            created_new = True
            print(f"  ✓ Created new Python scheduler: {scheduler.path()}")

        except Exception as e:
            print(f"  ✗ Cannot create new scheduler: {e}")
            print("  Fallback: Looking for existing schedulers...")

            # Strategy 2: Check the default scheduler on the topnet
            for parm_name in ["topscheduler", "defaultscheduler", "scheduler", "pdg_topscheduler"]:
                parm = self.topnet.parm(parm_name)
                if parm:
                    scheduler_path = parm.eval()
                    if scheduler_path:
                        # Handle both relative and absolute paths
                        if scheduler_path.startswith('/'):
                            # Absolute path
                            default_scheduler = hou.node(scheduler_path)
                        else:
                            # Relative path - resolve relative to topnet
                            default_scheduler = self.topnet.node(scheduler_path)

                        if default_scheduler:
                            scheduler = default_scheduler
                            print(f"  ✓ Found default scheduler: {scheduler.path()} ({scheduler.type().name()})")
                            break
                        else:
                            print(f"  Note: Default scheduler path '{scheduler_path}' not found")

            # Strategy 3: Search for Conductor schedulers (highest priority)
            if not scheduler:
                print("  Searching for Conductor schedulers...")
                for node in self.topnet.children():
                    node_type = node.type().name().lower()
                    if 'conductor' in node_type and 'scheduler' in node_type:
                        scheduler = node
                        print(f"  ✓ Found Conductor scheduler: {scheduler.path()} ({node.type().name()})")
                        break

            # Strategy 4: Search for Python schedulers
            if not scheduler:
                print("  Searching for Python schedulers...")
                for node in self.topnet.children():
                    if node.type().name() == 'pythonscheduler':
                        scheduler = node
                        print(f"  ✓ Found existing Python scheduler: {scheduler.path()}")
                        break

            # Strategy 5: Search for local schedulers
            if not scheduler:
                print("  Searching for local schedulers...")
                for node in self.topnet.children():
                    if node.type().name() == 'localscheduler':
                        scheduler = node
                        print(f"  ✓ Found existing local scheduler: {scheduler.path()}")
                        break

            # Strategy 6: Search for any other scheduler
            if not scheduler:
                print("  Searching for any scheduler...")
                for node in self.topnet.children():
                    if 'scheduler' in node.type().name().lower():
                        scheduler = node
                        print(f"  ✓ Found existing scheduler: {scheduler.path()} ({scheduler.type().name()})")
                        break

            # Debug: List all nodes in topnet if no scheduler found
            if not scheduler:
                print("\n  Debug: All nodes in TOP network:")
                for node in self.topnet.children():
                    node_type = node.type().name()
                    print(f"    - {node.name()} (type: {node_type})")
                print()

        if not scheduler:
            print("  ✗ No scheduler found or created")
            return None

        # Configure the scheduler
        try:
            # Set working directory if possible
            if scheduler.parm("pdg_workingdir"):
                scheduler.parm("pdg_workingdir").set("$HIP")
                print(f"  ✓ Set working directory on scheduler")

            # Determine scheduler type
            scheduler_type = scheduler.type().name().lower()

            # If we have custom code and it's a Python scheduler, set it

            if custom_code and 'conductor' in scheduler_type:
                if scheduler.parm("onschedule"):
                    scheduler.parm("onschedule").set(custom_code)
                    print(f"  ✓ Configured custom onSchedule code")
                elif scheduler.parm("submitasjob"):
                    # For submitAsJob mode
                    scheduler.parm("submitasjob").set(custom_code)
                    print(f"  ✓ Configured submitAsJob code")

            # For local schedulers
            elif 'local' in scheduler_type:
                print(f"  Note: Using local scheduler - custom code not applicable")
                # Local schedulers typically don't need custom code
                # They handle work items through their built-in logic

            else:
                print(f"  Note: Using {scheduler.type().name()} scheduler")

        except Exception as e:
            print(f"  Warning: Could not fully configure scheduler: {e}")

        return scheduler

    def _setup_scheduler_for_single_machine(self):
        """Create Python scheduler for single machine mode (no custom code)"""
        print("\n" + "-" * 60)
        print("Phase 4: Scheduler Setup (Single Machine - All Items)")
        print("-" * 60)

        try:
            # Use the helper to find or create a scheduler
            # For single machine mode, we don't need custom code
            self.scheduler = self._find_or_create_scheduler(
                preferred_types=['pythonscheduler', 'localscheduler', 'conductorscheduler'],
                custom_code=None  # No custom code needed for single machine mode
            )

            if not self.scheduler:
                print("✗ Failed to acquire scheduler")
                self.status_dict['errors'].append("Failed to acquire scheduler for single machine mode")
                return False

            # Apply scheduler to all nodes
            self._apply_scheduler_to_nodes()

            print("✓ Scheduler configured for single machine execution")
            return True

        except Exception as e:
            print(f"✗ Scheduler setup failed: {e}")
            self.status_dict['errors'].append(f"Scheduler setup: {e}")
            return False

    def _setup_scheduler_for_single_machine_local(self):
        """Create Local scheduler for proper out-of-process execution"""
        print("\n" + "-" * 60)
        print("Phase 4: Scheduler Setup (Single Machine - All Items)")
        print("-" * 60)

        try:
            print("\nScheduler acquisition strategy:")

            # Use Local Scheduler for standard local parallel execution
            scheduler_name = "temp_local_scheduler"

            # Remove any existing temp schedulers
            for node in self.topnet.children():
                if node.name().startswith("temp_") and "scheduler" in node.type().name():
                    try:
                        node.destroy()
                        print(f"  Removed existing temp scheduler: {node.name()}")
                    except:
                        pass

            # Create new Local Scheduler
            self.scheduler = self.topnet.createNode("localscheduler", scheduler_name)
            print(f"  ✓ Created new Local scheduler: {self.scheduler.path()}")

            # Configure working directory
            if self.scheduler.parm("workingdir"):
                self.scheduler.parm("workingdir").set(self.working_dir)
                print("  ✓ Set working directory on scheduler")

            # Set temp directory
            pdgtemp = os.path.join(self.working_dir, "pdgtemp")
            os.makedirs(pdgtemp, exist_ok=True)
            if self.scheduler.parm("tempdir"):
                self.scheduler.parm("tempdir").set(pdgtemp)

            # Configure for local execution - use all cores minus one
            if self.scheduler.parm("totalslotsmenu"):
                self.scheduler.parm("totalslotsmenu").set(1)  # CPU count - 1

            # Use temporary JSON for attribute passing
            if self.scheduler.parm("loadmethod"):
                self.scheduler.parm("loadmethod").set(0)  # Temporary JSON File
                print("  ✓ Set load method to Temporary JSON File")

            # Enable compression if available
            if self.scheduler.parm("compressdata"):
                self.scheduler.parm("compressdata").set(True)
                print("  ✓ Enabled work item data compression")

            print("  Note: Using localscheduler for default local execution behavior")

            # Apply scheduler to all nodes
            print("\nApplying scheduler to nodes:")
            scheduler_path = self.scheduler.path()
            count = 0

            # Apply to individual TOP nodes
            for node in self.topnet.children():
                if node.type().category().name() != "Top":
                    continue
                if node == self.scheduler:
                    continue

                # Try different parameter names
                for parm_name in ["topscheduler", "pdg_scheduler", "scheduler"]:
                    parm = node.parm(parm_name)
                    if parm:
                        try:
                            parm.set(scheduler_path)
                            print(f"  ✓ {node.name()} - set via '{parm_name}'")
                            count += 1
                            break
                        except:
                            pass

            # Set as network default
            for parm_name in ["topscheduler", "defaultscheduler"]:
                parm = self.topnet.parm(parm_name)
                if parm:
                    try:
                        parm.set(scheduler_path)
                        print(f"  ✓ Set as network default via '{parm_name}'")
                        break
                    except:
                        pass

            print(f"✓ Scheduler applied to {count} nodes")
            print("✓ Scheduler configured for single machine execution")

            return True

        except Exception as e:
            print(f"✗ Scheduler setup failed: {e}")
            self.status_dict['errors'].append(f"Scheduler setup: {e}")
            traceback.print_exc()
            return False

    def force_regenerate(self):
        """Force regeneration of tasks and work items"""
        print("Forcing task dirtiness / regeneration on TOP network...")

        try:
            # Clear any cached PDG context
            self.topnet.setPDGGraphContextProcessor(None)

            # Dirty the entire network
            self.topnet.dirtyAllTasks(True)
            print("Called topnet.dirtyAllTasks(True)")

            # Also dirty individual nodes, especially wedges
            for node in self.topnet.children():
                if node.type().category().name() != "Top":
                    continue

                try:
                    # Dirty the node
                    if hasattr(node, 'dirtyAllTasks'):
                        node.dirtyAllTasks(True)

                    # For wedge nodes, ensure attributes will be regenerated
                    if 'wedge' in node.type().name().lower():
                        pdg_node = node.getPDGNode()
                        if pdg_node:
                            # Clear all work items
                            if hasattr(pdg_node, 'dirtyAllWorkItems'):
                                pdg_node.dirtyAllWorkItems(True)
                            # Mark for regeneration
                            if hasattr(pdg_node, 'clearAllWorkItems'):
                                pdg_node.clearAllWorkItems()

                except:
                    pass

            # Give PDG time to process the dirty state
            time.sleep(0.5)

        except Exception as e:
            print(f"Warning during force regeneration: {e}")

    def generate_and_cook(self, block=True, tops_only=False):
        """
        Generate PDG graph (if needed) and cook work items.
        Ensures wedge variations and attributes are properly generated.
        """
        print("Generating PDG graph (if needed) and cooking work items...")
        cooked = False

        try:
            # CRITICAL: Force complete regeneration including wedge variations
            print("Forcing work item regeneration...")

            # Step 1: Dirty all tasks to force regeneration
            self.topnet.dirtyAllTasks(True)
            time.sleep(0.5)

            # Step 2: Find and explicitly generate wedge nodes BEFORE cooking
            print("Generating wedge variations...")
            for node in self.topnet.children():
                if node.type().category().name() != "Top":
                    continue

                node_type = node.type().name().lower()

                # Handle wedge nodes specifically
                if 'wedge' in node_type:
                    try:
                        # Get wedge count parameter
                        wedge_count = node.parm('wedgecount')
                        if wedge_count:
                            count = wedge_count.eval()
                            print(f"  Found wedge node '{node.name()}' with count: {count}")

                            # Force wedge to generate its variations
                            if hasattr(node, 'generateStaticWorkItems'):
                                node.generateStaticWorkItems()
                                print(f"    Generated static work items for wedge")

                            # Also try PDG node generation
                            pdg_node = node.getPDGNode()
                            if pdg_node:
                                if hasattr(pdg_node, 'regenerateStaticWorkItems'):
                                    pdg_node.regenerateStaticWorkItems()
                                elif hasattr(pdg_node, 'generateStaticWorkItems'):
                                    pdg_node.generateStaticWorkItems()
                                print(f"    Regenerated PDG work items for wedge")

                    except Exception as e:
                        print(f"    Warning: Could not generate wedge items: {e}")

                # Also handle any generator nodes
                elif any(gen in node_type for gen in ['generator', 'pattern', 'range']):
                    try:
                        if hasattr(node, 'generateStaticWorkItems'):
                            node.generateStaticWorkItems()
                            print(f"  Generated items for '{node.name()}'")
                    except:
                        pass

            # Step 3: Let generation propagate
            time.sleep(1)

            # Step 4: Now cook with proper PDG context
            print(f"Starting cookWorkItems(block={block}, tops_only={tops_only}) on topnet {self.topnet.path()}")

            try:
                # IMPORTANT: Use tops_only=False to ensure ROP nodes evaluate parameters correctly
                self.topnet.cookWorkItems(block=block, tops_only=tops_only)
                cooked = True
                print("PDG cookWorkItems completed.")
            except TypeError:
                print("cookWorkItems did not accept tops_only kw; calling without it.")
                self.topnet.cookWorkItems(block=block)
                cooked = True
                print("PDG cookWorkItems completed.")

        except Exception as e:
            print(f"Exception while cooking work items: {e}")
            traceback.print_exc()
            raise

        return cooked

    def _find_rop_target_from_topnet(self, ropfetch_node=None):
        """
        Robustly resolve a ROP target node from the topnet.
        If ropfetch_node (a ropfetch-type node) is given, try its 'roppath' parm first.
        Otherwise search beneath the TOP network for a ropfetch node, then try common /obj rop nodes.
        Returns a hou.Node or None.
        """
        rop_target = None

        # If an explicit ropfetch node is provided, try that first
        if ropfetch_node is not None:
            try:
                if ropfetch_node.parm("roppath"):
                    roppath = ropfetch_node.evalParm("roppath")
                    if roppath:
                        # try direct node resolution
                        rop_target = hou.node(roppath)
                        if not rop_target:
                            # try resolving relative to ropfetch parent
                            try:
                                parent = ropfetch_node.parent()
                                candidate = parent.path().rstrip("/") + "/" + roppath.lstrip("./")
                                rop_target = hou.node(candidate)
                            except Exception:
                                rop_target = None
            except Exception:
                rop_target = None
            if rop_target:
                return rop_target

        # Search for a ropfetch node under the topnet
        try:
            nodes_iter = getattr(self.topnet, "allSubChildren", None)
            nodes = nodes_iter() if callable(nodes_iter) else self.topnet.allNodes()
        except Exception:
            nodes = self.topnet.children()

        ropfetch = None
        for n in nodes:
            try:
                tname = n.type().name().lower()
            except Exception:
                tname = ""
            try:
                if "ropfetch" in tname or "ropfetch" in n.name().lower():
                    ropfetch = n
                    break
            except Exception:
                continue

        if ropfetch:
            try:
                if ropfetch.parm("roppath"):
                    rp = ropfetch.evalParm("roppath")
                    if rp:
                        rop_target = hou.node(rp) or hou.node(ropfetch.parent().path() + "/" + rp)
                        if rop_target:
                            return rop_target
            except Exception:
                pass

        # Generic search: find any ROP node anywhere in the scene
        # Search in common locations first
        search_roots = ["/obj", "/out", "/stage"]

        for root_path in search_roots:
            try:
                root = hou.node(root_path)
                if not root:
                    continue

                # Recursively search for ROP nodes
                for node in root.allSubChildren():
                    try:
                        node_type = node.type().name().lower()
                        # Check if it's a ROP node (any type)
                        if any(rop_type in node_type for rop_type in
                               ['rop_geometry', 'rop_alembic', 'rop_fbx', 'rop_comp',
                                'rop_mantra', 'rop_karma', 'usdrender', 'rop_gltf',
                                'rop_usd', 'rop_usdexport', 'filecache']):
                            return node
                    except Exception:
                        continue
            except Exception:
                continue

        return None

    def _extract_wedge_values_from_node(self, wedge_node, wedgecount):
        """
        Extract the actual wedge values from a wedge node.
        Returns a dict of attribute_name -> list of values
        """
        # First, try to get the wedge prefix/attribute name
        attrib_name = "w_seed"  # default
        for parm_name in ["prefix", "wedgeattribname", "attribname", "attribute"]:
            if wedge_node.parm(parm_name):
                name = wedge_node.evalParm(parm_name)
                if name:
                    attrib_name = name
                    break

        # Initialize values list
        values = []

        # CRITICAL: Check if this wedge is using random values
        # The wedge node in Houdini typically uses these parameter names
        is_random = False
        seed_value = 0

        # Check for random seed parameter (most wedge nodes have this)
        for seed_parm in ["randomseed", "seedvalue", "seed", "randseed"]:
            if wedge_node.parm(seed_parm):
                seed_value = wedge_node.evalParm(seed_parm)
                is_random = True
                print(f"    Found random seed parameter '{seed_parm}': {seed_value}")
                break

        # If we didn't find a seed param, check the wedge method
        if not is_random and wedge_node.parm("wedgemethod"):
            method = wedge_node.evalParm("wedgemethod")
            if method == 2:  # 2 = Random
                is_random = True
                # Get seed if available
                if wedge_node.parm("randomseed"):
                    seed_value = wedge_node.evalParm("randomseed")
                print(f"    Wedge method is Random, seed: {seed_value}")

        # If still not detected as random, check for the wedge type
        if not is_random:
            # Check if there's a "type" parameter set to random
            if wedge_node.parm("type"):
                wedge_type = wedge_node.evalParm("type")
                if wedge_type == 2 or str(wedge_type).lower() == "random":
                    is_random = True
                    print(f"    Wedge type indicates random")

        # IMPORTANT: For most wedge nodes, if there's no explicit method but there IS a seed,
        # it's likely using random values
        if not is_random and seed_value != 0:
            is_random = True
            print(f"    Detected random mode from non-zero seed value")

        if is_random:
            # Generate random values using the seed
            print(f"    Generating {wedgecount} random values with seed {seed_value}")
            random.seed(seed_value)
            for i in range(wedgecount):
                rand_val = random.random()
                values.append(str(rand_val))

            print(f"    Generated random values: {values[:3]}...")

        else:
            # Check if it's a range
            is_range = False
            start = 0
            end = 1

            if wedge_node.parm("wedgemethod"):
                method = wedge_node.evalParm("wedgemethod")
                if method == 1:  # 1 = Range
                    is_range = True

            if is_range or (wedge_node.parm("rangestart") and wedge_node.parm("rangeend")):
                is_range = True
                if wedge_node.parm("rangestart"):
                    start = wedge_node.evalParm("rangestart")
                if wedge_node.parm("rangeend"):
                    end = wedge_node.evalParm("rangeend")

                # Calculate step
                step = (end - start) / (wedgecount - 1) if wedgecount > 1 else 0

                for i in range(wedgecount):
                    values.append(str(start + step * i))

                print(f"    Generated {len(values)} range values from {start} to {end}")

            else:
                # Try to get explicit values
                found_values = False

                # Check for value list parameter
                for value_parm in ["values", "wedgevalues", "value"]:
                    if wedge_node.parm(value_parm):
                        raw = wedge_node.evalParm(value_parm)
                        if raw:
                            # Parse the values
                            vals = [v.strip() for v in re.split(r'[,\s]+', str(raw)) if v.strip()]
                            if vals:
                                values = vals
                                found_values = True
                                print(f"    Found explicit values: {values[:3]}...")
                                break

                # If no explicit values, use indices as last resort
                if not found_values:
                    values = [str(i) for i in range(wedgecount)]
                    print(f"    Using index values: 0 to {wedgecount - 1}")

        return {attrib_name: values}

    def _fallback_render_by_wedgecount(self):
        """
        Generic fallback when PDG generated 0 or 1 work items but wedge count > 1.
        """
        import random
        import re
        import traceback
        import os

        print("\n" + "=" * 60)
        print("WEDGE FALLBACK: Manual wedge rendering")
        print("=" * 60)

        # Initialize file tracking for collection
        if not hasattr(self, 'wedge_fallback_files'):
            self.wedge_fallback_files = []

        # Token regex
        TOKEN_RE = re.compile(r"`?@([A-Za-z0-9_]+)`?")

        # 1) Find wedge node
        wedge_node = None
        try:
            nodes_iter = getattr(self.topnet, "allSubChildren", None)
            nodes = nodes_iter() if callable(nodes_iter) else self.topnet.allNodes()
        except Exception:
            nodes = self.topnet.children()

        for n in nodes:
            try:
                tname = n.type().name().lower()
            except Exception:
                tname = ""
            try:
                if "wedge" in tname or "wedge" in n.name().lower():
                    wedge_node = n
                    break
            except Exception:
                continue

        if not wedge_node:
            print("Fallback: no wedge node found under topnet — cannot perform wedgecount fallback.")
            return False

        # 2) Read wedgecount
        wedgecount = None
        try:
            if wedge_node.parm("wedgecount"):
                wedgecount = int(wedge_node.evalParm("wedgecount"))
        except Exception:
            wedgecount = None

        if not wedgecount or wedgecount <= 0:
            print("Fallback: wedge node found but wedgecount is missing or zero.")
            return False

        print(f"✓ Found wedge node: {wedge_node.path()}")
        print(f"✓ Wedge count: {wedgecount}")
        print(f"  Wedge node type: {wedge_node.type().name()}")

        # DEBUG: List ALL parameters and their values
        print("\n  DEBUG - All wedge node parameters:")
        all_parms = {}
        try:
            for parm in wedge_node.parms():
                parm_name = parm.name()
                try:
                    parm_value = parm.eval()
                    all_parms[parm_name] = parm_value
                    # Only print parameters that might be relevant
                    if any(keyword in parm_name.lower() for keyword in
                           ['seed', 'method', 'random', 'value', 'prefix', 'attrib', 'type', 'mode', 'variation']):
                        print(f"    {parm_name} = {parm_value}")
                except:
                    pass
        except Exception as e:
            print(f"    Error listing parameters: {e}")

        # 3) Determine attribute name
        attrib_name = "w_seed"
        for parm_name in ["prefix", "wedgeattribname", "attribname", "attribute"]:
            if wedge_node.parm(parm_name):
                try:
                    name = wedge_node.evalParm(parm_name)
                    if name:
                        attrib_name = str(name).strip()
                        print(f"\n  Attribute name from '{parm_name}': {attrib_name}")
                        break
                except:
                    pass

        # 4) Generate wedge values
        token_value_lists = {}
        values = []
        is_random = False
        seed_value = None

        # Check for seedmethod (Labs wedge specific)
        if "seedmethod" in all_parms:
            seed_method = all_parms["seedmethod"]
            print(f"\n  Found seedmethod: {seed_method}")
            if seed_method > 0:  # Any non-zero value means variation
                is_random = True
                # Look for seed value
                if "seed" in all_parms:
                    seed_value = all_parms["seed"]
                    print(f"  Found seed: {seed_value}")

        # If not random yet, check for any seed parameter
        if not is_random:
            for seed_key in ['seed', 'randomseed', 'seedvalue', 'randseed']:
                if seed_key in all_parms:
                    val = all_parms[seed_key]
                    if val and val != 0:
                        is_random = True
                        seed_value = val
                        print(f"\n  Found {seed_key}: {seed_value} - using random mode")
                        break

        # FORCE RANDOM if we have a Labs wedge (as a last resort)
        if not is_random and "labs" in wedge_node.type().name().lower():
            print("\n  Labs wedge detected - forcing random mode with default seed")
            is_random = True
            seed_value = 12345

        # Generate values
        if is_random:
            if seed_value is None or seed_value == 0:
                seed_value = 12345
                print(f"  Using default seed: {seed_value}")

            print(f"\n  Generating {wedgecount} random values with seed {seed_value}")
            random.seed(int(seed_value))
            for i in range(wedgecount):
                rand_val = random.random()
                # FORMAT TO EXACTLY 6 DECIMAL PLACES
                formatted_val = f"{rand_val:.6f}"
                values.append(formatted_val)

            # Show values
            print(f"  Random values generated:")
            for i, v in enumerate(values[:5]):  # Show first 5
                print(f"    [{i}] = {v}")
            if len(values) > 5:
                print(f"    ... ({len(values) - 5} more)")
        else:
            # Fallback to indices
            values = [str(i) for i in range(wedgecount)]
            print(f"  Using index values: 0 to {wedgecount - 1}")

        # Store values
        token_value_lists[attrib_name] = values

        # Print token summary
        print(f"\n  Token '{attrib_name}': {values[0]}, {values[1]}, {values[2]}..." if len(
            values) >= 3 else f"  Token '{attrib_name}': {values}")

        # 5) Find ROP target
        rop_target = self._find_rop_target_from_topnet()
        if not rop_target:
            print("Fallback: could not locate a ROP target for wedge fallback.")
            return False

        print(f"\n✓ ROP target: {rop_target.path()}")

        # 6) Find output parameters
        candidate_parms = []
        for parmname in ["sopoutput", "sopoutput1", "output", "vm_picture", "sopoutputfile", "output_file"]:
            if rop_target.parm(parmname):
                candidate_parms.append(parmname)

        if not candidate_parms:
            print(f"Fallback: no known output parm found on rop target {rop_target.path()}")
            return False

        print(f"✓ Output parameters to substitute: {candidate_parms}")

        # 7) Render each wedge
        successful_renders = 0
        rendered_files = []

        for idx in range(wedgecount):
            print(f"\nRendering wedge {idx}/{wedgecount - 1}:")
            overrides = {}

            for parmname in candidate_parms:
                try:
                    parm = rop_target.parm(parmname)
                    try:
                        raw = parm.unexpandedString()
                    except:
                        raw = parm.eval()

                    if not raw:
                        continue

                    tokens = TOKEN_RE.findall(str(raw))
                    if not tokens:
                        continue

                    # Build token map
                    token_map = {}
                    for token in tokens:
                        if token in token_value_lists:
                            vals = token_value_lists[token]
                            token_map[token] = vals[idx] if idx < len(vals) else vals[-1]
                        else:
                            token_map[token] = str(idx)

                    # Substitute
                    new_val = str(raw)
                    for tk, tv in token_map.items():
                        new_val = new_val.replace(f"`@{tk}`", str(tv))
                        new_val = new_val.replace(f"@{tk}", str(tv))

                    if new_val != raw:
                        parm.set(new_val)
                        overrides[parmname] = raw
                        print(f"  ✓ {parmname}: '{raw}' -> '{new_val}'")

                        # Track file
                        try:
                            if hasattr(hou, 'text') and hasattr(hou.text, 'expandString'):
                                expanded = hou.text.expandString(new_val)
                            else:
                                expanded = hou.expandString(new_val)

                            if not os.path.isabs(expanded):
                                expanded = os.path.join(os.path.dirname(self.hip_file), expanded)

                            rendered_files.append(expanded)
                        except:
                            pass
                except Exception as e:
                    print(f"  ✗ Error with {parmname}: {e}")

            # Render
            try:
                if hasattr(rop_target, "render"):
                    rop_target.render()
                else:
                    import hou
                    hou.Rop.render(rop_target)
                print(f"  ✓ Render completed for wedge {idx}")
                successful_renders += 1
            except Exception as e:
                print(f"  ✗ Render failed for wedge {idx}: {e}")

            # Restore parameters
            for pname, original in overrides.items():
                try:
                    rop_target.parm(pname).set(original)
                except:
                    pass

        # Store tracked files
        self.wedge_fallback_files = rendered_files

        print(f"\n✓ Wedge fallback complete: {successful_renders}/{wedgecount} successful renders")
        print(f"✓ Tracked {len(self.wedge_fallback_files)} output files for collection")

        # Update status
        if hasattr(self, 'status_dict'):
            self.status_dict['work_items_total'] = wedgecount
            self.status_dict['work_items_succeeded'] = successful_renders
            self.status_dict['work_items_failed'] = wedgecount - successful_renders
            self.status_dict['wedge_fallback_used'] = True
            self.status_dict['wedge_fallback_files'] = self.wedge_fallback_files

        return successful_renders > 0

    def _execute_single_machine(self):
        """Execute all work items on single machine (like right-click Cook Node)"""
        print("\n" + "-" * 60)
        print("Phase 5: Single Machine Execution (Cook All Items)")
        print("-" * 60)

        try:
            print("Initializing PDG context for local execution...")

            # REMOVED: This method doesn't exist on TopNode objects
            # self.topnet.setPDGGraphContextProcessor(None)

            # Force complete regeneration
            self.force_regenerate()

            # Pre-generate wedge work items to get accurate count
            print("\nPre-generating wedge and generator nodes...")
            self._pre_generate_work_items()

            # Count after pre-generation
            initial_count = self._count_all_work_items()
            print(f"Initial work item count after pre-generation: {initial_count}")

            # Now cook everything
            print("\nGenerating and cooking all work items...")
            print(f"  Output node: {self.output_node.name() if self.output_node else 'Network level'}")

            cook_start = time.time()
            cooked = self.generate_and_cook(block=True, tops_only=False)

            # Wait and recount
            time.sleep(1)
            total_items = self._count_all_work_items()
            print(f"✓ Generated {total_items} work items")

            # Check if we need the wedge fallback
            wedge_fallback_triggered = False
            if total_items <= 1:
                # Look for wedge nodes with count > 1
                wedge_count = self._get_wedge_count()
                if wedge_count and wedge_count > 1:
                    print(f"\n⚠ Only {total_items} work item(s) but wedge count is {wedge_count}")
                    print("Triggering wedge fallback mechanism...")
                    if self._fallback_render_by_wedgecount():
                        wedge_fallback_triggered = True
                        total_items = wedge_count
                elif initial_count <= 1:
                    print("\n⚠ Only 1 work item detected, attempting alternate generation...")
                    cooked = self._try_alternate_generation()
                    time.sleep(1)
                    total_items = self._count_all_work_items()
                    print(f"  After alternate generation: {total_items} work items")

            elapsed = time.time() - cook_start
            print(f"\nLocal cooking completed in {elapsed:.2f} seconds")

            if total_items > 0 and not wedge_fallback_triggered:
                succeeded = self._count_successful_items()
                failed = self._count_failed_items()
                print(f"Results: {succeeded} succeeded, {failed} failed out of {total_items} total")

                # Update status dict
                self.status_dict['work_items_total'] = total_items
                self.status_dict['work_items_succeeded'] = succeeded
                self.status_dict['work_items_failed'] = failed

            print(
                f"✓ Success rate: {(self.status_dict.get('work_items_succeeded', 0) / total_items * 100) if total_items > 0 else 0:.1f}%")
            return True

        except Exception as e:
            print(f"✗ Single machine execution failed: {e}")
            self.status_dict['errors'].append(f"Single machine execution: {e}")
            traceback.print_exc()
            return False

    def _get_wedge_count(self):
        """Get the wedge count from any wedge node in the network"""
        try:
            for node in self.topnet.children():
                if node.type().category().name() != "Top":
                    continue
                node_type = node.type().name().lower()
                if 'wedge' in node_type:
                    wedge_count_parm = node.parm('wedgecount')
                    if wedge_count_parm:
                        return wedge_count_parm.eval()
        except Exception:
            pass
        return None

    def _pre_generate_work_items(self):
        """Pre-generate work items from wedge and generator nodes"""
        generated_nodes = []

        for node in self.topnet.children():
            if node.type().category().name() != "Top":
                continue

            node_type = node.type().name().lower()

            # Priority 1: Wedge nodes
            if 'wedge' in node_type:
                try:
                    # Ensure wedge parameters are set
                    if node.parm('wedgecount'):
                        wedge_count = node.parm('wedgecount').eval()

                        # Check for seed parameter with @w_seed pattern
                        seed_method = node.parm('seedmethod')
                        if seed_method and seed_method.eval() > 0:  # Not "No Variation"
                            print(f"  Wedge '{node.name()}' configured for {wedge_count} variations")

                        # Generate the wedge variations
                        pdg_node = node.getPDGNode()
                        if pdg_node:
                            # Clear and regenerate
                            if hasattr(pdg_node, 'dirtyAllWorkItems'):
                                pdg_node.dirtyAllWorkItems(True)
                            if hasattr(pdg_node, 'regenerateStaticWorkItems'):
                                pdg_node.regenerateStaticWorkItems()

                            generated_nodes.append(node.name())
                            print(f"    ✓ Pre-generated wedge variations for '{node.name()}'")

                except Exception as e:
                    print(f"    Could not pre-generate wedge '{node.name()}': {e}")

            # Priority 2: Generator nodes
            elif any(gen in node_type for gen in ['generator', 'pattern', 'range', 'partition']):
                try:
                    if hasattr(node, 'generateStaticWorkItems'):
                        node.generateStaticWorkItems()
                        generated_nodes.append(node.name())
                        print(f"  ✓ Pre-generated items for '{node.name()}'")
                except:
                    pass

        if generated_nodes:
            print(f"  Pre-generated nodes: {', '.join(generated_nodes)}")
            time.sleep(0.5)  # Allow generation to propagate

        return generated_nodes

    def _try_alternate_generation(self):
        """Try alternate generation approach for stubborn wedge nodes"""
        print("  Trying alternate wedge generation approach...")

        try:
            # Method 1: Cook wedge node directly
            wedge_nodes = []
            for node in self.topnet.children():
                if 'wedge' in node.type().name().lower():
                    wedge_nodes.append(node)

            for wedge_node in wedge_nodes:
                try:
                    print(f"    Cooking wedge node '{wedge_node.name()}' directly...")

                    # Get the PDG node
                    pdg_node = wedge_node.getPDGNode()
                    if pdg_node:
                        # Try cooking it directly
                        if hasattr(pdg_node, 'cook'):
                            pdg_node.cook(block=True)

                        # Check work items
                        if hasattr(pdg_node, 'workItems'):
                            count = len(pdg_node.workItems)
                            print(f"      Wedge now has {count} work items")

                except Exception as e:
                    print(f"      Failed: {e}")

            # Method 2: Cook from the output node
            if self.output_node:
                print(f"    Cooking from output node '{self.output_node.name()}'...")
                try:
                    self.output_node.executeGraph(False, True, False, True)
                    return True
                except:
                    try:
                        self.output_node.cookWorkItems(block=True)
                        return True
                    except:
                        pass

            # Method 3: Force complete graph regeneration
            print("    Forcing complete graph regeneration...")
            self.topnet.dirtyAllTasks(True)
            time.sleep(0.5)
            return self.topnet.cookWorkItems(block=True, tops_only=False)

        except Exception as e:
            print(f"    Alternate generation failed: {e}")
            return False

    def _identify_output_node(self):
        """Identify the output node - same logic Houdini uses for Cook Output Node"""
        if self.output_node:
            return  # Already identified

        print("\nIdentifying output node:")

        # Priority 1: Node with display flag set
        try:
            display_node = self.topnet.displayNode()
            if display_node and display_node.type().category().name() == "Top":
                self.output_node = display_node
                print(f"✓ Using display node: {self.output_node.name()}")
                return
        except:
            pass

        # Priority 2: Check for nodes with display flag set (alternative method)
        for node in self.topnet.children():
            if node.type().category().name() != "Top":
                continue
            try:
                if hasattr(node, 'isDisplayFlagSet') and node.isDisplayFlagSet():
                    self.output_node = node
                    print(f"✓ Using display flagged node: {self.output_node.name()}")
                    return
            except:
                pass

        # Priority 3: Find typical output nodes
        output_nodes = []
        for node in self.topnet.children():
            if node.type().category().name() != "Top":
                continue

            # Use helper method to check if it's an output node
            if self._is_output_node(node):
                output_nodes.append(node)

        if output_nodes:
            # Prefer nodes with "output" in the name
            for node in output_nodes:
                if "output" in node.type().name().lower():
                    self.output_node = node
                    print(f"✓ Using output-type node: {self.output_node.name()}")
                    return

            # Otherwise use the first ROP/output node found
            self.output_node = output_nodes[0]
            print(f"✓ Using output node: {self.output_node.name()}")
            return

        # Priority 4: Find the last node in the chain (likely the output)
        # Look for nodes with no nodes depending on them
        leaf_nodes = []
        for node in self.topnet.children():
            if node.type().category().name() != "Top":
                continue
            if "scheduler" in node.type().name().lower():
                continue

            # Check if any other nodes depend on this one
            has_dependents = False
            for other_node in self.topnet.children():
                if other_node == node:
                    continue
                if other_node.type().category().name() != "Top":
                    continue

                # Check inputs
                try:
                    inputs = other_node.inputs()
                    if node in inputs:
                        has_dependents = True
                        break
                except:
                    pass

            if not has_dependents:
                leaf_nodes.append(node)

        if leaf_nodes:
            self.output_node = leaf_nodes[0]
            print(f"✓ Using leaf node as output: {self.output_node.name()}")
            return

        # Fallback: Just use the first non-scheduler TOP node
        for node in self.topnet.children():
            if node.type().category().name() == "Top" and "scheduler" not in node.type().name().lower():
                self.output_node = node
                print(f"✓ Using first TOP node as output: {self.output_node.name()}")
                return

        print("⚠ No suitable output node found, will cook at network level")

    def _count_successful_items(self):
        """Count successfully completed work items"""
        succeeded = 0

        try:
            for node in self.topnet.children():
                if node.type().category().name() != "Top":
                    continue

                try:
                    pdg_node = node.getPDGNode()
                    if not pdg_node:
                        continue

                    # Get work items
                    work_items = pdg_node.workItems if hasattr(pdg_node, 'workItems') else []

                    for wi in work_items:
                        # Check if item is successful using multiple methods
                        is_success = False

                        # Method 1: Check state attribute
                        if hasattr(wi, 'state'):
                            try:
                                import pdg
                                if wi.state == pdg.workItemState.CookedSuccess:
                                    is_success = True
                            except:
                                pass

                        # Method 2: Check isSuccessful method
                        if not is_success and hasattr(wi, 'isSuccessful'):
                            try:
                                if wi.isSuccessful():
                                    is_success = True
                            except:
                                # Sometimes it's a property, not a method
                                if wi.isSuccessful:
                                    is_success = True

                        # Method 3: Check isCooked and not failed
                        if not is_success and hasattr(wi, 'isCooked'):
                            try:
                                is_cooked = wi.isCooked() if callable(wi.isCooked) else wi.isCooked
                                is_failed = False
                                if hasattr(wi, 'isFailed'):
                                    is_failed = wi.isFailed() if callable(wi.isFailed) else wi.isFailed

                                if is_cooked and not is_failed:
                                    is_success = True
                            except:
                                pass

                        if is_success:
                            succeeded += 1

                except Exception as e:
                    # Continue counting even if one node fails
                    continue

        except Exception as e:
            print(f"Warning: Error counting successful items: {e}")

        return succeeded

    def _count_failed_items(self):
        """Count failed work items"""
        failed = 0

        try:
            for node in self.topnet.children():
                if node.type().category().name() != "Top":
                    continue

                try:
                    pdg_node = node.getPDGNode()
                    if not pdg_node:
                        continue

                    # Get work items
                    work_items = pdg_node.workItems if hasattr(pdg_node, 'workItems') else []

                    for wi in work_items:
                        # Check if item failed using multiple methods
                        is_failed = False

                        # Method 1: Check state attribute
                        if hasattr(wi, 'state'):
                            try:
                                import pdg
                                if wi.state == pdg.workItemState.CookedFail:
                                    is_failed = True
                            except:
                                pass

                        # Method 2: Check isFailed method
                        if not is_failed and hasattr(wi, 'isFailed'):
                            try:
                                if wi.isFailed():
                                    is_failed = True
                            except:
                                # Sometimes it's a property, not a method
                                if wi.isFailed:
                                    is_failed = True

                        # Method 3: Check state string
                        if not is_failed and hasattr(wi, 'state'):
                            try:
                                state_str = str(wi.state).lower()
                                if 'fail' in state_str or 'error' in state_str:
                                    is_failed = True
                            except:
                                pass

                        if is_failed:
                            failed += 1

                except Exception as e:
                    # Continue counting even if one node fails
                    continue

        except Exception as e:
            print(f"Warning: Error counting failed items: {e}")

        return failed

    def _count_all_work_items(self):
        """Count total number of work items (already exists but here's an improved version)"""
        total = 0

        try:
            for node in self.topnet.children():
                if node.type().category().name() != "Top":
                    continue

                # Skip scheduler nodes
                if "scheduler" in node.type().name().lower():
                    continue

                try:
                    pdg_node = node.getPDGNode()
                    if not pdg_node:
                        continue

                    # Get work items using multiple methods
                    work_items = None

                    # Method 1: Direct workItems attribute
                    if hasattr(pdg_node, 'workItems'):
                        work_items = pdg_node.workItems

                    # Method 2: allWorkItems method
                    if not work_items and hasattr(pdg_node, 'allWorkItems'):
                        try:
                            work_items = pdg_node.allWorkItems()
                        except:
                            pass

                    # Method 3: staticWorkItems for static nodes
                    if not work_items and hasattr(pdg_node, 'staticWorkItems'):
                        try:
                            work_items = pdg_node.staticWorkItems
                        except:
                            pass

                    if work_items:
                        count = len(work_items)
                        if count > 0:
                            total += count

                except Exception as e:
                    # Continue counting even if one node fails
                    continue

        except Exception as e:
            print(f"Warning: Error counting total items: {e}")

        return total

    def _get_work_items_details(self):
        """Get detailed information about all work items (optional helper method)"""
        details = []

        try:
            for node in self.topnet.children():
                if node.type().category().name() != "Top":
                    continue

                try:
                    pdg_node = node.getPDGNode()
                    if not pdg_node or not hasattr(pdg_node, 'workItems'):
                        continue

                    for wi in pdg_node.workItems:
                        item_info = {
                            'node': node.name(),
                            'index': wi.index if hasattr(wi, 'index') else -1,
                            'name': wi.name if hasattr(wi, 'name') else 'unknown',
                            'id': wi.id if hasattr(wi, 'id') else -1,
                        }

                        # Get status
                        if hasattr(wi, 'state'):
                            try:
                                import pdg
                                if wi.state == pdg.workItemState.CookedSuccess:
                                    item_info['status'] = 'success'
                                elif wi.state == pdg.workItemState.CookedFail:
                                    item_info['status'] = 'failed'
                                elif wi.state == pdg.workItemState.Cooking:
                                    item_info['status'] = 'cooking'
                                elif wi.state == pdg.workItemState.Waiting:
                                    item_info['status'] = 'waiting'
                                else:
                                    item_info['status'] = str(wi.state)
                            except:
                                item_info['status'] = 'unknown'

                        # Get outputs if available
                        try:
                            if hasattr(wi, 'expectedOutputFiles'):
                                item_info['outputs'] = list(wi.expectedOutputFiles)
                            elif hasattr(wi, 'outputFiles'):
                                item_info['outputs'] = list(wi.outputFiles)
                        except:
                            pass

                        details.append(item_info)

                except Exception as e:
                    continue

        except Exception as e:
            print(f"Warning: Error getting work item details: {e}")

        return details

    def _collect_single_machine_results(self):
        """Collect results from single machine execution"""
        print("\nCollecting single machine execution results...")

        total_items = 0
        succeeded_items = 0
        failed_items = 0
        work_items_details = []

        for node in self.topnet.children():
            if node.type().category().name() != "Top":
                continue

            try:
                pdg_node = node.getPDGNode()
                if not pdg_node:
                    continue

                work_items = pdg_node.workItems
                node_succeeded = 0
                node_failed = 0

                for wi in work_items:
                    total_items += 1

                    # Determine status
                    status = 'unknown'
                    if hasattr(wi, 'isSuccessful') and wi.isSuccessful:
                        status = 'success'
                        succeeded_items += 1
                        node_succeeded += 1
                    elif hasattr(wi, 'isFailed') and wi.isFailed:
                        status = 'failed'
                        failed_items += 1
                        node_failed += 1
                    elif hasattr(wi, 'isCancelled') and wi.isCancelled:
                        status = 'cancelled'
                        failed_items += 1
                        node_failed += 1

                    work_items_details.append({
                        'node': node.name(),
                        'item_name': wi.name,
                        'item_index': wi.index if hasattr(wi, 'index') else -1,
                        'status': status
                    })

                if len(work_items) > 0:
                    print(f"  {node.name()}: {len(work_items)} items "
                          f"(✓ {node_succeeded} succeeded, ✗ {node_failed} failed)")

            except Exception as e:
                print(f"  Warning: Could not get work items from {node.name()}: {e}")

        # Update status dictionary
        self.status_dict['work_items_total'] = total_items
        self.status_dict['work_items_succeeded'] = succeeded_items
        self.status_dict['work_items_failed'] = failed_items
        self.status_dict['work_items_details'] = work_items_details

        print(f"\nTotal work items: {total_items}")
        print(f"  Succeeded: {succeeded_items}")
        print(f"  Failed: {failed_items}")
        print(f"  Success rate: {(succeeded_items / total_items * 100) if total_items > 0 else 0:.1f}%")

    def _execute_full_graph(self):
        """Execute the full PDG graph using topcook.py"""
        print("\n" + "-" * 60)
        print("Phase 5: Full Graph Execution")
        print("-" * 60)

        hip_dir = os.path.dirname(self.hip_file)

        # Use hython directly
        hython_path = "hython"

        # Construct the command to cook the PDG graph
        topcook_script = os.path.expandvars("$HHP/pdgjob/topcook.py")
        topcook_script = topcook_script.replace("\\", "/")

        # Build the command with valid arguments
        cmd = [
            hython_path,
            topcook_script,
            "--hip", self.hip_file,
            "--toppath", self.topnet_path,
            "--verbosity", "3",  # Maximum verbosity
            "--report", "items",  # Report on individual work items
            "--keepopen", "error"  # Keep session open on error
        ]

        # Add task graph output
        output_file = os.path.join(hip_dir, f"{os.path.basename(self.hip_file)}.post.py")
        cmd.extend(["--taskgraphout", output_file])

        # Set up environment variables
        env = os.environ.copy()
        env['PDG_DIR'] = hip_dir
        env['PDG_VERBOSE'] = '3'
        env['HOUDINI_PDG_NODE_DEBUG'] = '3'

        try:
            print("=" * 60)
            print(f"Starting PDG graph cook at: {self.topnet_path}")
            print(f"Hip file: {self.hip_file}")
            print(f"PDG_DIR set to: {hip_dir}")
            print(f"Command: {' '.join(cmd)}")
            print("=" * 60)

            # Run the command with real-time output
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                universal_newlines=True,
                env=env
            )

            # Stream output in real-time
            output_lines = []
            error_lines = []
            failed_items = {}
            successful_items = []
            current_node = None

            # Read stdout
            for line in iter(process.stdout.readline, ''):
                if line:
                    print(line.rstrip())
                    output_lines.append(line)

                    # Parse node context
                    if "Node " in line and "Given Node" not in line:
                        current_node = line.split("Node ")[-1].strip()

                    # Capture failed work items
                    if "CookedFail" in line:
                        parts = line.strip().split()
                        if parts:
                            item_name = parts[0]
                            failed_items[item_name] = current_node
                            self.status_dict['cook_result']['failed_items'].append({
                                'name': item_name,
                                'node': current_node
                            })

                    # Capture successful work items
                    if "CookedSuccess" in line:
                        parts = line.strip().split()
                        if parts:
                            item_name = parts[0]
                            successful_items.append(item_name)
                            self.status_dict['cook_result']['successful_items'].append({
                                'name': item_name,
                                'node': current_node
                            })

                    # Capture warnings
                    if "warning" in line.lower():
                        self.status_dict['cook_result']['warnings'].append(line.strip())

            # Read stderr
            for line in iter(process.stderr.readline, ''):
                if line:
                    print(f"STDERR: {line.rstrip()}")
                    error_lines.append(line)

            # Wait for process to complete
            return_code = process.wait()
            self.status_dict['cook_result']['return_code'] = return_code

            print("=" * 60)

            # Analyze results
            if failed_items:
                print("FAILED WORK ITEMS:")
                print("-" * 40)
                for item_name, node_name in failed_items.items():
                    print(f"  {item_name} (from node: {node_name})")
                print("-" * 40)

            if successful_items:
                print(f"\n✓ Successfully cooked {len(successful_items)} work items")

            if self.status_dict['cook_result']['warnings']:
                print("\nWarnings:")
                for warning in self.status_dict['cook_result']['warnings'][:5]:  # Show first 5
                    print(f"  {warning}")

            if return_code == 0:
                print("\nCook completed")
                if failed_items:
                    print(f"WARNING: {len(failed_items)} work items failed")
                else:
                    print("SUCCESS: All work items cooked successfully!")
                return True
            else:
                print(f"\nERROR: PDG graph cooking failed with return code: {return_code}")
                return False

        except Exception as e:
            print(f"✗ Graph execution failed: {e}")
            self.status_dict['errors'].append(f"Graph execution: {e}")
            traceback.print_exc()
            return False

    def _collect_full_graph_results(self):
        """Collect results from full graph execution"""
        print("\nCollecting full graph execution results...")

        total_items = 0
        succeeded_items = 0
        failed_items = 0
        work_items_details = []

        for node in self.topnet.children():
            if node.type().category().name() != "Top":
                continue

            try:
                pdg_node = node.getPDGNode()
                if not pdg_node:
                    continue

                work_items = pdg_node.workItems
                node_succeeded = 0
                node_failed = 0

                for wi in work_items:
                    total_items += 1

                    # Determine status
                    status = 'unknown'
                    if hasattr(wi, 'isSuccessful') and wi.isSuccessful:
                        status = 'success'
                        succeeded_items += 1
                        node_succeeded += 1
                    elif hasattr(wi, 'isFailed') and wi.isFailed:
                        status = 'failed'
                        failed_items += 1
                        node_failed += 1
                    elif hasattr(wi, 'isCancelled') and wi.isCancelled:
                        status = 'cancelled'
                        failed_items += 1
                        node_failed += 1

                    work_items_details.append({
                        'node': node.name(),
                        'item_name': wi.name,
                        'item_index': wi.index if hasattr(wi, 'index') else -1,
                        'status': status
                    })

                if len(work_items) > 0:
                    print(f"  {node.name()}: {len(work_items)} items "
                          f"(✓ {node_succeeded} succeeded, ✗ {node_failed} failed)")

            except Exception as e:
                print(f"  Warning: Could not get work items from {node.name()}: {e}")

        # Update status dictionary
        self.status_dict['work_items_total'] = total_items
        self.status_dict['work_items_succeeded'] = succeeded_items
        self.status_dict['work_items_failed'] = failed_items
        self.status_dict['work_items_details'] = work_items_details

        print(f"\nTotal work items: {total_items}")
        print(f"  Succeeded: {succeeded_items}")
        print(f"  Failed: {failed_items}")
        print(f"  Success rate: {(succeeded_items / total_items * 100) if total_items > 0 else 0:.1f}%")

    def _setup_scheduler_for_full_graph(self):
        """Create and configure the Python scheduler for full graph execution"""
        print("\n" + "-" * 60)
        print("Phase 4: Scheduler Setup (Full Graph)")
        print("-" * 60)

        try:
            # Prepare submitAsJob code (optional for full graph)
            submit_as_job_code = '''# Submit As Job callback for full graph execution
# This runs when the entire graph is submitted as a single job
import subprocess
import os

# Default behavior - just execute the command
job_env = os.environ.copy()
job_env['PDG_DIR'] = str(self.workingDir(False))
job_env['PDG_TEMP'] = str(self.tempDir(False))
job_env['PDG_SCRIPTDIR'] = str(self.scriptDir(False))

print(f"[SCHEDULER] Executing full graph cook")
return True
'''

            # Use the helper to find or create a scheduler
            self.scheduler = self._find_or_create_scheduler(
                preferred_types=['conductorscheduler', 'pythonscheduler', 'localscheduler'],
                custom_code=submit_as_job_code
            )

            if not self.scheduler:
                print("✗ Failed to acquire scheduler")
                self.status_dict['errors'].append("Failed to acquire scheduler for full graph")
                return False

            # Apply scheduler to all nodes
            self._apply_scheduler_to_nodes()

            print("✓ Scheduler configured for full graph execution")
            return True

        except Exception as e:
            print(f"✗ Scheduler setup failed: {e}")
            self.status_dict['errors'].append(f"Scheduler setup: {e}")
            return False

    def _setup_scheduler(self):
        """Create and configure the Python scheduler for single work item mode"""
        print("\n" + "-" * 60)
        print("Phase 4: Scheduler Setup (Single Work Item)")
        print("-" * 60)

        try:
            # Generate custom onSchedule code for single item execution
            on_schedule_code = self._generate_on_schedule_code()

            # Use the helper to find or create a scheduler
            self.scheduler = self._find_or_create_scheduler(
                preferred_types=['conductorscheduler', 'pythonscheduler', 'localscheduler'],
                custom_code=on_schedule_code
            )

            if not self.scheduler:
                print("✗ Failed to acquire scheduler")
                self.status_dict['errors'].append("Failed to acquire scheduler for single work item")
                return False

            print(f"✓ Configured to cook only work item at index {self.item_index}")

            # Apply scheduler to all nodes
            self._apply_scheduler_to_nodes()

            return True

        except Exception as e:
            print(f"✗ Scheduler setup failed: {e}")
            self.status_dict['errors'].append(f"Scheduler setup: {e}")
            return False

    def _generate_on_schedule_code(self):
        """Generate the onSchedule callback code"""
        return f'''# Custom onSchedule for single work item execution
import subprocess
import os
import sys

TARGET_INDEX = {self.item_index}

print(f"[SCHEDULER] Item {{work_item.index}}: {{work_item.name}}")

if work_item.index == TARGET_INDEX:
    print(f"[SCHEDULER] COOKING work item index={{work_item.index}}")

    # Prepare work item
    self.createJobDirsAndSerializeWorkItems(work_item)

    # Expand command tokens
    item_command = self.expandCommandTokens(work_item.command, work_item)

    # Setup environment
    job_env = os.environ.copy()

    job_env['PDG_RESULT_SERVER'] = str(self.workItemResultServerAddr())
    job_env['PDG_ITEM_NAME'] = str(work_item.name)
    job_env['PDG_ITEM_ID'] = str(work_item.id)
    # job_env['PDG_DIR'] = str(self.workingDir(False))
    job_env['PDG_TEMP'] = str(self.tempDir(False))
    # job_env['PDG_SCRIPTDIR'] = str(self.scriptDir(False))

    # Execute command
    print(f"[SCHEDULER] Executing: {{item_command}}...")
    returncode = subprocess.call(item_command, shell=True, env=job_env)

    print(f"[SCHEDULER] Completed with return code: {{returncode}}")

    if returncode == 0:
        return pdg.scheduleResult.CookSucceeded
    return pdg.scheduleResult.CookFailed
else:
    print(f"[SCHEDULER] SKIPPING work item index={{work_item.index}}")
    return pdg.scheduleResult.Skip
'''

    def _apply_scheduler_to_nodes(self):
        """Apply scheduler to all TOP nodes"""
        print("\nApplying scheduler to nodes:")

        scheduler_path = self.scheduler.path()
        count = 0

        # Apply to individual nodes
        for node in self.topnet.children():
            if node.type().category().name() != "Top":
                continue
            if "scheduler" in node.type().name().lower():
                continue

            # Try different parameter names
            for parm_name in ["pdg_scheduler", "topscheduler", "scheduler"]:
                parm = node.parm(parm_name)
                if parm:
                    try:
                        parm.set(scheduler_path)
                        print(f"  ✓ {node.name()} - set via '{parm_name}'")
                        count += 1
                        break
                    except:
                        pass

        # Set as default on network
        for parm_name in ["topscheduler", "defaultscheduler", "scheduler"]:
            parm = self.topnet.parm(parm_name)
            if parm:
                try:
                    parm.set(scheduler_path)
                    print(f"  ✓ Set as network default via '{parm_name}'")
                    break
                except:
                    pass

        print(f"✓ Scheduler applied to {count} nodes")

    def _execute_work_items(self):
        """Generate and execute work items for single item mode"""
        print("\n" + "-" * 60)
        print("Phase 5: Work Item Execution (Single Item)")
        print("-" * 60)

        try:
            # Initialize PDG context
            print("Initializing PDG context...")
            self._initialize_pdg_context()

            # Generate work items
            print("\nGenerating work items...")
            num_items = self._generate_work_items()

            if num_items == 0:
                print("✗ No work items generated")
                self.status_dict['errors'].append("No work items generated")
                return False

            print(f"✓ Generated {num_items} work items")

            if num_items <= self.item_index:
                print(f"⚠ Warning: Target index {self.item_index} >= {num_items} items")

            # Cook work items
            print(f"\nCooking work items (target index: {self.item_index})...")

            try:
                if self.output_node:
                    self.output_node.cookWorkItems(block=True)
                else:
                    self.topnet.cookWorkItems(block=True)
                print("✓ Cooking completed")
            except Exception as e:
                print(f"⚠ Cooking raised exception (may be normal): {e}")
                # Continue anyway as some items may have cooked

            # Collect work item results after cooking
            self._collect_work_item_results()

            print("✓ Work item execution completed")
            return True

        except Exception as e:
            print(f"✗ Work item execution failed: {e}")
            self.status_dict['errors'].append(f"Execution: {e}")

            # Try alternative cooking methods
            return self._try_alternative_cooking()


    def _initialize_pdg_context(self):
        """Initialize PDG graph context"""
        # Dirty all nodes
        for node in self.topnet.children():
            if node.type().category().name() == "Top":
                try:
                    node.dirtyAllTasks(False)
                except:
                    pass

        time.sleep(0.5)

        # Try to generate on a generator node
        for node in self.topnet.children():
            if "generator" in node.type().name().lower():
                try:
                    node.generateStaticWorkItems()
                    time.sleep(0.5)
                    return
                except:
                    pass

    def _generate_work_items(self):
        """Generate work items and count them"""
        max_items = 0

        # First, try to generate work items at the network level
        print("  Attempting network-level generation...")
        try:
            self.topnet.cookWorkItems(generate_only=True, block=True)
            time.sleep(1)
            print("    ✓ Network-level generation completed")
        except Exception as e:
            print(f"    Note: Network generation returned: {e}")

        # Also try to generate on individual nodes
        print("  Generating on individual nodes...")
        for node in self.topnet.children():
            if node.type().category().name() != "Top":
                continue
            if "scheduler" in node.type().name().lower():
                continue

            try:
                # Try to generate static work items
                if hasattr(node, 'generateStaticWorkItems'):
                    node.generateStaticWorkItems()
                    print(f"    Generated static items for {node.name()}")
            except:
                pass

            try:
                # Try cook with generate_only
                if hasattr(node, 'cookWorkItems'):
                    node.cookWorkItems(generate_only=True, block=True)
                    print(f"    Generated items for {node.name()}")
            except:
                pass

        # Wait for generation to complete
        time.sleep(1)

        # Now count work items on each node
        print("\n  Counting generated work items:")
        for node in self.topnet.children():
            if node.type().category().name() != "Top":
                continue
            if "scheduler" in node.type().name().lower():
                continue

            try:
                # Try multiple methods to get work items
                work_items = None
                pdg_node = None

                # Method 1: Direct PDG node
                try:
                    pdg_node = node.getPDGNode()
                    if pdg_node and hasattr(pdg_node, 'workItems'):
                        work_items = pdg_node.workItems
                except:
                    pass

                # Method 2: Through graph context
                if not work_items:
                    try:
                        graph_context = node.getPDGGraphContext()
                        if graph_context:
                            pdg_node = node.getPDGNode()
                            if pdg_node:
                                work_items = pdg_node.workItems
                    except:
                        pass

                if work_items and len(work_items) > 0:
                    print(f"    {node.name()}: {len(work_items)} items")
                    max_items = max(max_items, len(work_items))

                    # Debug: print first few work item indices
                    indices = []
                    for wi in work_items[:5]:
                        if hasattr(wi, 'index'):
                            indices.append(wi.index)
                    if indices:
                        print(f"      Sample indices: {indices}")
            except Exception as e:
                print(f"    Error counting items in {node.name()}: {e}")

        return max_items

    def _collect_work_item_results(self):
        """Collect results from work items - Fixed version for proper processed/skipped tracking"""
        print("\nCollecting work item results...")

        # Clear the lists to ensure clean collection
        self.status_dict['work_items_processed'] = []
        self.status_dict['skipped_items'] = []

        # First, make sure we have generated work items
        for node in self.topnet.children():
            if node.type().category().name() != "Top":
                continue

            # Skip scheduler nodes
            if "scheduler" in node.type().name().lower():
                continue

            try:
                # Try multiple ways to get PDG node and work items
                pdg_node = None
                work_items = []

                # Method 1: Direct PDG node access
                try:
                    pdg_node = node.getPDGNode()
                    if pdg_node:
                        work_items = pdg_node.workItems
                        if work_items:
                            print(f"  Found {len(work_items)} work items in {node.name()} via getPDGNode")
                except Exception as e:
                    pass

                # Method 2: Try through graph context
                if not work_items:
                    try:
                        graph_context = node.getPDGGraphContext()
                        if graph_context:
                            pdg_node = graph_context.graph.nodeByName(node.name())
                            if pdg_node:
                                work_items = pdg_node.workItems
                                if work_items:
                                    print(f"  Found {len(work_items)} work items in {node.name()} via graph context")
                    except Exception as e:
                        pass

                # Method 3: Use pdg module directly
                if not work_items:
                    try:
                        import pdg
                        for context_name in dir(pdg):
                            if "Context" in context_name:
                                context = getattr(pdg, context_name)
                                if hasattr(context, 'graph'):
                                    try:
                                        test_node = context.graph.nodeByName(node.name())
                                        if test_node and hasattr(test_node, 'workItems'):
                                            work_items = test_node.workItems
                                            if work_items:
                                                pdg_node = test_node
                                                print(
                                                    f"  Found {len(work_items)} work items in {node.name()} via pdg module")
                                                break
                                    except:
                                        pass
                    except Exception as e:
                        pass

                # Process work items if we found any
                if work_items:
                    for i, wi in enumerate(work_items):
                        # Try to get index from work item
                        wi_index = i  # Default to enumeration index

                        # Try to get actual work item index
                        if hasattr(wi, 'index'):
                            wi_index = wi.index
                        elif hasattr(wi, 'id'):
                            # Sometimes index is stored as id
                            wi_index = wi.id

                        # Get work item name
                        wi_name = wi.name if hasattr(wi, 'name') else f"{node.name()}_{i}"

                        # Collect work item information
                        item_info = {
                            'index': wi_index,
                            'name': wi_name,
                            'node': node.name(),
                            'status': self._get_work_item_status(wi)
                        }

                        # Check if this matches our target index
                        if wi_index == self.item_index:
                            self.status_dict['work_items_processed'].append(item_info)
                            print(f"    ✓ Processed: {wi_name} (index: {wi_index}) - {item_info['status']}")
                        else:
                            self.status_dict['skipped_items'].append(item_info)
                            # Only print first few skipped to avoid clutter
                            if len(self.status_dict['skipped_items']) <= 3:
                                print(f"    - Skipped: {wi_name} (index: {wi_index})")
                else:
                    # No work items found for this node
                    print(f"  No work items found in {node.name()}")

            except Exception as e:
                print(f"  Warning: Error collecting from {node.name()}: {str(e)}")
                import traceback
                traceback.print_exc()
                continue

        # Print summary
        processed_count = len(self.status_dict['work_items_processed'])
        skipped_count = len(self.status_dict['skipped_items'])

        print(f"\nWork Item Collection Summary:")
        print(f"  Target Index: {self.item_index}")
        print(f"  Frame Number: {str(self.item_index).zfill(4) if self.item_index is not None else '0000'}")
        print(f"  Processed: {processed_count} work item(s)")
        print(f"  Skipped: {skipped_count} work item(s)")

        if processed_count == 0 and skipped_count == 0:
            print(f"  ⚠ Warning: No work items were found at all!")
            print(f"    This might mean work items weren't generated properly")
            print(f"    or the PDG context isn't accessible")
        elif processed_count == 0:
            print(f"  ⚠ Warning: No work items found with index {self.item_index}")
            available_indices = sorted(
                set([item['index'] for item in self.status_dict['skipped_items'] if item['index'] >= 0]))
            if available_indices:
                print(f"    Available indices: {available_indices[:10]}...")
        else:
            # Show detailed status for processed items
            for item in self.status_dict['work_items_processed']:
                print(f"    - {item['name']} from {item['node']}: {item['status']}")

    def _get_work_item_status(self, wi):
        """Get work item status string"""
        if hasattr(wi, 'isSuccessful') and wi.isSuccessful:
            return 'success'
        elif hasattr(wi, 'isFailed') and wi.isFailed:
            return 'failed'
        elif hasattr(wi, 'isCancelled') and wi.isCancelled:
            return 'cancelled'
        else:
            return 'unknown'

    def _try_alternative_cooking(self):
        """Try alternative cooking methods"""
        print("\nTrying alternative cooking methods...")

        # Method 1: executeGraph
        try:
            if self.output_node:
                self.output_node.executeGraph(False, True, False, True)
                print("✓ Alternative method 1 succeeded")
                return True
        except:
            pass

        # Method 2: Direct network cook
        try:
            self.topnet.cookWorkItems(block=True)
            print("✓ Alternative method 2 succeeded")
            return True
        except:
            pass

        print("✗ All cooking methods failed")
        return False

    def clean_path(self, current_path):
        """
        Prepares a file path by expanding environment variables, normalizing slashes, removing
        drive letters.

        Args:
            current_path (str): The file path to prepare.

        Returns:
            str: The prepared file path, quoted and normalized, or the original path on error.
        """
        try:
            if not current_path:
                return f'{current_path}'

            current_path = script_path = re.sub("^[a-zA-Z]:", "", current_path).replace("\\", "/")
            return f'{current_path}'
        except Exception as e:
            print(f"Error preparing path: {current_path}, {e}")
            return f'{current_path}'

    def _collect_all_outputs(self):
        """Comprehensive output file collection"""
        print("\n" + "-" * 60)
        print("Phase 6: Output Collection")
        print("-" * 60)

        collectors = [
            ('USD Files', self._collect_usd_files, 'usd'),
            ('Rendered Images', self._collect_render_files, 'renders'),
            ('PDG Files', self._collect_pdg_files, 'pdg'),
            ('Log Files', self._collect_log_files, 'logs'),
            ('Geo Files', self._collect_log_files, 'geo'),
            ('Work Item Outputs', self._collect_work_item_outputs, 'other'),
            ('Wedge Fallback Outputs', self._collect_wedge_fallback_files, 'wedge_outputs')  # NEW
        ]

        for name, collector, category in collectors:
            print(f"\nCollecting {name}...")
            try:
                files = collector()
                count = 0
                for src_file in files:
                    dest = self._copy_file_organized(src_file, category)
                    if dest:
                        self.status_dict['files_created'][category].append(dest)
                        count += 1
                print(f"  ✓ Collected {count} {name.lower()}")
            except Exception as e:
                print(f"  ✗ Failed to collect {name}: {e}")

        # Update total count
        total = sum(len(v) for k, v in self.status_dict['files_created'].items()
                    if k != 'total_count')
        self.status_dict['files_created']['total_count'] = total

        print(f"\n✓ Total files collected: {total}")

    def _collect_wedge_fallback_files(self):
        """Collect files generated by wedge fallback mechanism"""
        files = []

        # Check if wedge fallback was used and files were generated
        if hasattr(self, 'wedge_fallback_files') and self.wedge_fallback_files:
            for filepath in self.wedge_fallback_files:
                if os.path.exists(filepath):
                    files.append(filepath)
                    print(f"  Found: {os.path.basename(filepath)}")

        # Also scan the geo directory for any files we might have missed
        # This is a backup in case file tracking didn't work perfectly
        if not files and hasattr(self, 'status_dict') and self.status_dict.get('wedge_fallback_used'):
            geo_dir = os.path.join(os.path.dirname(self.hip_file), 'geo')
            if os.path.exists(geo_dir):
                import glob
                # Look for files with the wedge pattern (containing decimal numbers)
                for pattern in ['*.bgeo.sc', '*.bgeo', '*.geo']:
                    for filepath in glob.glob(os.path.join(geo_dir, f'*[0-9].[0-9]*{pattern}')):
                        files.append(filepath)
                        print(f"  Found (scan): {os.path.basename(filepath)}")

        return files

    def _collect_usd_files(self):
        """Collect all USD files"""
        patterns = [
            os.path.join(self.working_dir, '**/*.usd'),
            os.path.join(self.working_dir, '**/*.usda'),
            os.path.join(self.working_dir, '**/*.usdc'),
            os.path.join(self.working_dir, '**/*.usdz'),
        ]

        files = []
        for pattern in patterns:
            files.extend(glob.glob(pattern, recursive=True))

        return list(set(files))  # Remove duplicates

    def _collect_render_files(self):
        """Collect all rendered images"""
        patterns = [
            '/tmp/render/**/*.exr',
            '/tmp/render/**/*.png',
            '/tmp/render/**/*.jpg',
            '/tmp/render/**/*.tif',
            os.path.join(self.working_dir, 'render/**/*.exr'),
            os.path.join(self.working_dir, 'images/**/*'),
        ]

        files = []
        for pattern in patterns:
            try:
                files.extend(glob.glob(pattern, recursive=True))
            except:
                # Non-recursive fallback for /tmp
                if pattern.startswith('/tmp'):
                    files.extend(glob.glob(pattern.replace('/**/', '/')))

        return list(set(files))

    def _collect_pdg_files(self):
        """Collect PDG-specific files"""
        pdgtemp_dir = os.path.join(self.working_dir, 'pdgtemp')
        if not os.path.exists(pdgtemp_dir):
            return []

        patterns = [
            os.path.join(pdgtemp_dir, '**/*.json'),
            os.path.join(pdgtemp_dir, '**/data/*'),
        ]

        files = []
        for pattern in patterns:
            files.extend(glob.glob(pattern, recursive=True))

        return files

    def _collect_log_files(self):
        """Collect log files"""
        patterns = [
            os.path.join(self.working_dir, '**/*.log'),
            os.path.join(self.working_dir, 'pdgtemp/**/*.txt'),
        ]

        files = []
        for pattern in patterns:
            files.extend(glob.glob(pattern, recursive=True))

        return files

    def _collect_work_item_outputs(self):
        """Collect outputs from work items"""
        files = []

        # First, try to collect from PDG work items
        if self.topnet:
            try:
                for node in self.topnet.children():
                    if node.type().category().name() != "Top":
                        continue

                    try:
                        pdg_node = node.getPDGNode()
                        if not pdg_node:
                            continue

                        work_items = pdg_node.workItems
                        for wi in work_items:
                            # Try multiple methods to get output files
                            for attr in ['expectedOutputFiles', 'actualOutputFiles', 'outputFiles']:
                                try:
                                    output_files = getattr(wi, attr)
                                    for f in output_files:
                                        file_path = f.path if hasattr(f, 'path') else str(f)

                                        # Expand __PDG_DIR__ token
                                        if "__PDG_DIR__" in file_path:
                                            pdg_dir = os.environ.get("PDG_DIR", self.working_dir)
                                            file_path = file_path.replace("__PDG_DIR__", pdg_dir)

                                        # Check if file exists
                                        if os.path.exists(file_path):
                                            files.append(file_path)
                                            print(f"    Found work item output: {os.path.basename(file_path)}")
                                except:
                                    pass
                    except:
                        pass
            except:
                pass

        # Also scan common output directories as fallback
        if len(files) == 0:
            print("    No outputs from work items, scanning directories...")

            # Scan geo directory
            geo_dir = os.path.join(self.working_dir, 'geo')
            if os.path.exists(geo_dir):
                import glob
                for pattern in ['*.bgeo', '*.bgeo.sc', '*.bgeo.gz', '*.geo']:
                    geo_files = glob.glob(os.path.join(geo_dir, pattern))
                    for gf in geo_files:
                        # Skip wedge fallback files if they exist
                        if hasattr(self, 'wedge_fallback_files') and gf in self.wedge_fallback_files:
                            continue
                        files.append(gf)
                        print(f"    Found in geo dir: {os.path.basename(gf)}")

            # Scan render directory
            render_dir = os.path.join(self.working_dir, 'render')
            if os.path.exists(render_dir):
                import glob
                for pattern in ['*.exr', '*.png', '*.jpg', '*.tif']:
                    render_files = glob.glob(os.path.join(render_dir, '**', pattern), recursive=True)
                    files.extend(render_files)

            # Scan USD directory
            usd_dir = os.path.join(self.working_dir, 'usd')
            if os.path.exists(usd_dir):
                import glob
                for pattern in ['*.usd', '*.usda', '*.usdc']:
                    usd_files = glob.glob(os.path.join(usd_dir, pattern))
                    files.extend(usd_files)

        # Remove duplicates while preserving order
        seen = set()
        unique_files = []
        for f in files:
            if f not in seen:
                seen.add(f)
                unique_files.append(f)

        return unique_files

    def _copy_file_organized(self, src_file, category):
        """Copy file to organized output structure"""
        if not os.path.exists(src_file):
            return None

        # Skip if file is already in output dir
        if src_file.startswith(self.output_dir):
            return None

        # Create category directory
        dest_dir = os.path.join(self.output_dir, category)
        os.makedirs(dest_dir, exist_ok=True)

        # Generate unique destination name
        filename = os.path.basename(src_file)
        dest_path = os.path.join(dest_dir, filename)

        if os.path.exists(dest_path):
            base, ext = os.path.splitext(filename)
            counter = 1
            while os.path.exists(dest_path):
                dest_path = os.path.join(dest_dir, f"{base}_{counter}{ext}")
                counter += 1

        try:
            shutil.copy2(src_file, dest_path)
            return dest_path
        except Exception as e:
            print(f"    Failed to copy {filename}: {e}")
            return None

    def _save_final_hip(self):
        """Save the final HIP file"""
        print("\n" + "-" * 60)
        print("Phase 7: Save HIP File")
        print("-" * 60)

        try:
            import tempfile

            # Build filename based on mode
            hip_name = os.path.basename(self.hip_file)
            base, ext = os.path.splitext(hip_name)

            if self.cook_entire_graph:
                # Submit As Job mode: save with timestamp
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                final_filename = f"{base}_submitasjob_{timestamp}{ext}"
            elif self.use_single_machine:
                # Single Machine mode: save with timestamp
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                final_filename = f"{base}_single_machine_{timestamp}{ext}"
            else:
                # On Schedule mode: save with frame number
                frame_num = str(self.item_index).zfill(4)
                final_filename = f"{base}_final.{frame_num}{ext}"

            # Create temp file path
            temp_dir = "/tmp"
            if not os.path.exists(temp_dir):
                temp_dir = tempfile.gettempdir()

            temp_hip_path = os.path.join(temp_dir, final_filename)

            # Build final destination path
            final_hip_dir = os.path.join(self.output_dir, 'hip')
            final_hip_path = os.path.join(final_hip_dir, final_filename)

            print(f"  Saving to temp location: {temp_hip_path}")

            # Save to temp location first
            hou.hipFile.save(temp_hip_path)
            print(f"  ✓ HIP file saved to temp location")

            # Ensure output directory exists
            os.makedirs(final_hip_dir, exist_ok=True)
            print(f"  ✓ Output directory ready: {final_hip_dir}")

            # Copy from temp to final location
            print(f"  Copying to final location: {final_hip_path}")
            shutil.copy2(temp_hip_path, final_hip_path)
            print(f"  ✓ HIP file copied to final location")

            # Clean up temp file
            try:
                os.remove(temp_hip_path)
                print(f"  ✓ Cleaned up temp file")
            except Exception as cleanup_error:
                print(f"  Warning: Could not clean up temp file: {cleanup_error}")

            # Update status tracking
            self.status_dict['files_created']['hip'].append(final_hip_path)

            print(f"✓ Final HIP file saved: {final_hip_path}")

        except Exception as e:
            print(f"✗ Failed to save HIP file: {e}")
            self.status_dict['errors'].append(f"HIP save: {e}")

            # Clean up temp file if it exists
            try:
                if 'temp_hip_path' in locals() and os.path.exists(temp_hip_path):
                    os.remove(temp_hip_path)
                    print(f"  ✓ Cleaned up temp file after error")
            except:
                pass

    def _finalize_execution(self):
        """Finalize execution and write status"""
        print("\n" + "-" * 60)
        print("Phase 8: Finalization")
        print("-" * 60)

        # Calculate duration
        self.status_dict['timestamp_end'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            start = datetime.strptime(self.status_dict['timestamp_start'], "%Y-%m-%d %H:%M:%S")
            end = datetime.strptime(self.status_dict['timestamp_end'], "%Y-%m-%d %H:%M:%S")
            self.status_dict['duration_seconds'] = (end - start).total_seconds()
        except:
            self.status_dict['duration_seconds'] = 0

        # Write status file
        status_dir = os.path.join(self.output_dir, 'execution_status')
        os.makedirs(status_dir, exist_ok=True)

        if self.cook_entire_graph:
            # Submit As Job mode: save with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            status_file = os.path.join(status_dir, f'pdg_submitasjob_status_{timestamp}.json')
        elif self.use_single_machine:
            # Single Machine mode: save with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            status_file = os.path.join(status_dir, f'pdg_single_machine_status_{timestamp}.json')
        else:
            # On Schedule mode: save with frame number
            frame_num = str(self.item_index).zfill(4)
            status_file = os.path.join(status_dir, f'pdg_execution_status.{frame_num}.json')

        try:
            with open(status_file, 'w') as f:
                json.dump(self.status_dict, f, indent=4, default=str)
            print(f"✓ Status written to: {status_file}")

            # Create a symlink to latest
            latest_link = os.path.join(status_dir, 'pdg_execution_status.latest.json')
            try:
                if os.path.exists(latest_link):
                    os.remove(latest_link)
                os.symlink(os.path.basename(status_file), latest_link)
                print(f"  Created latest link: {latest_link}")
            except:
                pass

        except Exception as e:
            print(f"✗ Failed to write status: {e}")

        # Print summary
        print("\n" + "=" * 80)
        print("EXECUTION SUMMARY")
        print("=" * 80)
        print(f"Execution Mode: {self.execution_mode.upper()}")
        print(f"Status: {self.status_dict['status'].upper()}")
        print(f"Duration: {self.status_dict['duration_seconds']:.2f} seconds")

        if self.cook_entire_graph or self.use_single_machine:
            print(f"Total Work Items: {self.status_dict.get('work_items_total', 0)}")
            print(f"  Succeeded: {self.status_dict.get('work_items_succeeded', 0)}")
            print(f"  Failed: {self.status_dict.get('work_items_failed', 0)}")
        else:
            print(f"Frame/Item Index: {self.item_index} (Frame: {str(self.item_index).zfill(4)})")
            print(f"Work Items Processed: {len(self.status_dict.get('work_items_processed', []))}")
            print(f"Work Items Skipped: {len(self.status_dict.get('skipped_items', []))}")

        print(f"Files Collected: {self.status_dict['files_created']['total_count']}")

        if self.status_dict['errors']:
            print(f"\nErrors ({len(self.status_dict['errors'])}):")
            for error in self.status_dict['errors']:
                print(f"  - {error}")

        print("=" * 80)


def main():
    """Main entry point"""
    # Parse arguments
    parser = argparse.ArgumentParser(
        description='PDG Universal Wrapper Script for Conductor render farm'
    )
    parser.add_argument('--hip_file', type=str, required=True,
                        help='Path to the Houdini file')
    parser.add_argument('--topnet_path', type=str, default='/obj/topnet1',
                        help='Path to the TOP network node')
    parser.add_argument('--working_dir', type=str, required=True,
                        help='Working directory path')
    parser.add_argument('--output_dir', type=str, default=None,
                        help='Output directory for rendered files')

    # Mode selection arguments
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--cook_entire_graph', action='store_true',
                       help='Cook entire graph (submitAsJob mode)')
    group.add_argument('--use_single_machine', action='store_true',
                       help='Cook all work items on single machine (local execution)')
    group.add_argument('--item_index', type=int, default=None,
                       help='Index of the work item to cook (on_schedule mode)')

    args = parser.parse_args()

    # Validate mode
    if not args.cook_entire_graph and not args.use_single_machine and args.item_index is None:
        parser.error("One of --cook_entire_graph, --use_single_machine, or --item_index must be specified")

    # Determine output directory

    if not args.output_dir:
        args.output_dir = os.path.join(args.working_dir, 'pdg_render')

    # Create and run executor
    executor = PDGUniversalExecutor(
        hip_file=args.hip_file,
        topnet_path=args.topnet_path,
        working_dir=args.working_dir,
        output_dir=args.output_dir,
        item_index=args.item_index,
        cook_entire_graph=args.cook_entire_graph,
        use_single_machine=args.use_single_machine
    )

    success = executor.run()

    # Exit with appropriate code
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()