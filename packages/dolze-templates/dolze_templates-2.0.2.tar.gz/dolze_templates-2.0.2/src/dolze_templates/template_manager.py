"""
Template Manager Module

This module provides the core template management functionality for Dolze templates.
It centralizes template operations and provides a clean API for template manipulation.
"""

import json
import os
import pkgutil
from typing import Dict, Any, Optional, List

try:
    from jinja2 import Environment, BaseLoader
except ImportError:
    # Fallback if Jinja2 is not available
    Environment = None
    BaseLoader = None

from .template_registry import TemplateRegistry
from .page_manager import PageManager
from .navigation_manager import NavigationManager
from .ui_component_manager import UIComponentManager
from .asset_manager import AssetManager

class PackageLoader(BaseLoader):
    """Custom Jinja2 loader for package templates"""
    
    def __init__(self, package_name: str):
        self.package_name = package_name
    
    def get_source(self, environment, template):
        try:
            source = pkgutil.get_data(self.package_name, template)
            if source is None:
                raise FileNotFoundError(f"Template {template} not found")
            return source.decode('utf-8'), template, lambda: True
        except Exception as e:
            raise FileNotFoundError(f"Template {template} not found: {e}")

class TemplateManager:
    """
    Main class for managing templates in the Dolze system.
    
    This class provides methods for retrieving templates, managing pages,
    and handling template rendering operations.
    """
    
    def __init__(self):
        """Initialize the TemplateManager with TemplateRegistry, PageManager, NavigationManager, UIComponentManager, and AssetManager instances."""
        self.registry = TemplateRegistry()
        self.page_manager = PageManager()
        self.navigation_manager = NavigationManager()
        self.ui_component_manager = UIComponentManager()
        self.asset_manager = AssetManager()
        # Cache for template content
        self._template_content_cache = {}
        
        # Initialize Jinja2 environment if available
        if Environment is not None:
            from jinja2 import Undefined
            self.jinja_env = Environment(
                loader=PackageLoader('dolze_templates'),
                autoescape=True,
                undefined=Undefined
            )
            # Add built-in functions to global context
            self.jinja_env.globals.update({
                'range': range,
                'len': len,
                'enumerate': enumerate,
                'str': str,
                'int': int,
                'float': float,
                'bool': bool,
                'list': list,
                'dict': dict,
                'zip': zip,
                'map': map,
                'filter': filter,
                'sorted': sorted,
                'reversed': reversed,
                'min': min,
                'max': max,
                'sum': sum,
                'abs': abs,
                'round': round
            })
        else:
            self.jinja_env = None
    

    def get_page_config(self, template_id: str, page_type: str) -> Optional[Dict[str, Any]]:
        """
        Get the configuration for a page in a template.
        
        Args:
            template_id (str): The ID of the template.
            page_type (str): The type of page.
            
        Returns:
            Optional[Dict[str, Any]]: The page configuration, or None if not found.
        """
        return self.page_manager.get_page_config(template_id, page_type)
    
    def get_template_by_id(self, template_id: str) -> Dict[str, Any]:
        """
        Get a template configuration by its ID.
        
        Args:
            template_id (str): The ID of the template.
            
        Returns:
            Dict[str, Any]: The template configuration.
            
        Raises:
            ValueError: If the template ID is not found in the registry.
        """
        template_config = self.registry.get_template_config(template_id)
        if not template_config:
            raise ValueError(f"Template '{template_id}' not found in registry")
        return template_config
    
    def get_available_pages_for_template(self, template_id: str) -> List[str]:
        """
        Get a list of available pages for a template.
        
        Args:
            template_id (str): The ID of the template.
            
        Returns:
            List[str]: List of page slugs available for the template.
            
        Raises:
            ValueError: If the template ID is not found in the registry.
        """
        template_config = self.get_template_by_id(template_id)
        return list(template_config.get("pages", {}).keys())
    
    def get_section_variants(self, template_id: str, page: str = "index") -> Optional[Dict[str, str]]:
        """
        Get section variants for a template and page.
        
        Args:
            template_id (str): The ID of the template.
            page (str, optional): The page slug. Defaults to "index".
            
        Returns:
            Optional[Dict[str, str]]: A dictionary mapping section names to variant IDs,
                                     or None if not found.
        """
        template_config = self.get_template_by_id(template_id)
        if "section_variants" in template_config and page in template_config["section_variants"]:
            return template_config["section_variants"][page]
        return None
    
    def get_template_content(self, template_path: str) -> str:
        """
        Get the content of a template file.
        
        Args:
            template_path (str): The path to the template file.
            
        Returns:
            str: The content of the template file.
            
        Raises:
            ValueError: If the template file cannot be loaded.
        """
        if template_path in self._template_content_cache:
            return self._template_content_cache[template_path]
        
        try:
            # Normalize the path
            normalized_path = template_path.replace('templates/', '')
            
            # Use pkgutil to get the template content
            data = pkgutil.get_data('dolze_templates', f'templates/{normalized_path}')
            if data:
                content = data.decode('utf-8')
                self._template_content_cache[template_path] = content
                return content
            else:
                raise ValueError(f"Could not load template: {template_path}")
        except Exception as e:
            raise ValueError(f"Failed to load template: {template_path}, error: {e}")
    
    def check_section_variant_exists(self, section_name: str, variant: str) -> bool:
        """
        Check if a section variant exists in the package.
        
        Args:
            section_name (str): The name of the section.
            variant (str): The variant ID (e.g., "v1", "v2").
            
        Returns:
            bool: True if the variant exists, False otherwise.
        """
        try:
            section_path = f"sections/{section_name}/{variant}.html"
            # Try to get the content, if it succeeds, the variant exists
            data = pkgutil.get_data('dolze_templates', f'templates/{section_path}')
            return data is not None
        except Exception:
            return False
    
    def get_sample_json(self) -> Dict[str, Any]:
        """
        Get the sample JSON data.
        
        Returns:
            Dict[str, Any]: The sample JSON data.
            
        Raises:
            ValueError: If the sample JSON cannot be loaded.
        """
        try:
            # Use pkgutil to get the sample JSON
            data = pkgutil.get_data('dolze_templates', 'sample.json')
            if data:
                return json.loads(data.decode('utf-8'))
            else:
                raise ValueError("Could not load sample JSON")
        except Exception as e:
            raise ValueError(f"Failed to load sample JSON: {e}")
    
    def derive_template_id(self, business_config: Dict[str, Any]) -> str:
        """
        Derive a template ID from business configuration.
        
        Args:
            business_config (Dict[str, Any]): The business configuration.
            
        Returns:
            str: The derived template ID.
        """
        # Default template to fall back to if constructed template doesn't exist
        DEFAULT_TEMPLATE = "brand_service_digital_saas"
        
        # Extract business configuration
        biz_type = business_config.get("biz_type", "").lower()
        offering = business_config.get("offering", "").lower()
        channel = business_config.get("channel", "").lower()
        
        # Construct template ID from business configuration
        if biz_type and offering and channel:
            constructed_template = f"{biz_type}_{offering}_{channel}"
            
            try:
                # Check if the template exists in the registry
                if self.registry.template_exists(constructed_template):
                    return constructed_template
            except Exception:
                pass
        
        # Return default template if constructed template doesn't exist or there was an error
        return DEFAULT_TEMPLATE
    
    def add_page_to_template(self, template_id: str, page_type: str, page_title: str = None, content: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Add a page to a template.
        
        Args:
            template_id (str): The ID of the template.
            page_type (str): The type of page to add (e.g., "shop", "privacy").
            page_title (str, optional): Custom title for the page. Defaults to None.
            content (Dict[str, Any], optional): Custom content for the page. Defaults to None.
            
        Returns:
            Dict[str, Any]: The configuration for the new page.
            
        Raises:
            ValueError: If the template doesn't exist or the page type is not recognized.
        """
        # Check if the template exists
        if not self.registry.template_exists(template_id):
            raise ValueError(f"Template '{template_id}' not found")
            
        # Create the page configuration
        page_config = self.page_manager.create_page(template_id, page_type, content)
        
        # Create a navigation item for the page
        nav_item = self.page_manager.add_page_to_navigation(template_id, page_type, page_title)
        
        # Get default section variants for the page
        section_variants = self.page_manager.get_default_variants_for_page(template_id, page_type)
        
        # Return the complete page configuration
        return {
            "config": page_config,
            "navigation": nav_item,
            "section_variants": section_variants
        }
    
    def remove_page_from_template(self, template_id: str, page_type: str) -> bool:
        """
        Remove a page from a template.
        
        Args:
            template_id (str): The ID of the template.
            page_type (str): The type of page to remove (e.g., "shop", "privacy").
            
        Returns:
            bool: True if the page was removed successfully, False otherwise.
        """
        # Check if the template exists
        if not self.registry.template_exists(template_id):
            raise ValueError(f"Template '{template_id}' not found")
        
        # Remove the page configuration
        self.page_manager.remove_page(template_id, page_type)
        
        # Remove the navigation item for the page
        self.page_manager.remove_page_from_navigation(template_id, page_type)
        
        return True
    
    def update_page_in_template(self, template_id: str, page_type: str, page_title: str = None, content: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Update a page in a template.
        
        Args:
            template_id (str): The ID of the template.
            page_type (str): The type of page to update (e.g., "shop", "privacy").
            page_title (str, optional): Custom title for the page. Defaults to None.
            content (Dict[str, Any], optional): Custom content for the page. Defaults to None.
            
        Returns:
            Dict[str, Any]: The updated page configuration.
            
        Raises:
            ValueError: If the template doesn't exist or the page type is not recognized.
        """
        # Check if the template exists
        if not self.registry.template_exists(template_id):
            raise ValueError(f"Template '{template_id}' not found")
        
        # Update the page configuration
        page_config = self.page_manager.update_page(template_id, page_type, content)
        
        # Update the navigation item for the page
        nav_item = self.page_manager.update_page_in_navigation(template_id, page_type, page_title)
        
        # Return the updated page configuration
        return {
            "config": page_config,
            "navigation": nav_item
        }
        
    # Navigation Management Methods
    
    def get_navigation_config(self, template_id: str) -> Optional[Dict[str, Any]]:
        """
        Get the navigation configuration for a template.
        
        Args:
            template_id (str): The ID of the template.
            
        Returns:
            Optional[Dict[str, Any]]: The navigation configuration, or None if not found.
        """
        return self.navigation_manager.get_navigation_config(template_id)
    
    def get_navigation_items(self, template_id: str) -> List[Dict[str, Any]]:
        """
        Get the navigation items for a template.
        
        Args:
            template_id (str): The ID of the template.
            
        Returns:
            List[Dict[str, Any]]: List of navigation items.
        """
        return self.navigation_manager.get_navigation_items(template_id)
    

    def generate_navigation(self, template_id: str, pages: List[str] = None) -> Dict[str, Any]:
        """
        Generate a navigation configuration for a template.
        
        Args:
            template_id (str): The ID of the template.
            pages (List[str], optional): List of page slugs to include in the navigation. 
                                        If None, all available pages will be included.
            
        Returns:
            Dict[str, Any]: The generated navigation configuration.
        """
        if pages is None:
            # Get all available pages for the template
            pages = self.get_available_pages_for_template(template_id)
            
        return self.navigation_manager.generate_navigation_for_pages(template_id, pages)
    
    # UI Component Management Methods
    
    def get_component_config(self, component_type: str, variant: str = "default") -> Dict[str, Any]:
        """
        Get the configuration for a UI component.
        
        Args:
            component_type (str): The type of component (e.g., "button", "cta").
            variant (str, optional): The variant of the component. Defaults to "default".
            
        Returns:
            Dict[str, Any]: The component configuration.
        """
        return self.ui_component_manager.get_component_config(component_type, variant)
    
    def get_available_component_types(self) -> List[str]:
        """
        Get a list of available UI component types.
        
        Returns:
            List[str]: List of available component type names.
        """
        return self.ui_component_manager.get_available_component_types()
    
    def get_available_variants(self, component_type: str) -> List[str]:
        """
        Get a list of available variants for a UI component type.
        
        Args:
            component_type (str): The type of component.
            
        Returns:
            List[str]: List of available variant names.
        """
        return self.ui_component_manager.get_available_variants(component_type)
    
    def create_button(self, label: str, url: str, variant: str = "primary", 
                     additional_classes: str = "", attributes: Dict[str, str] = None) -> Dict[str, Any]:
        """
        Create a button configuration.
        
        Args:
            label (str): The button label text.
            url (str): The URL the button links to.
            variant (str, optional): The button variant. Defaults to "primary".
            additional_classes (str, optional): Additional CSS classes. Defaults to "".
            attributes (Dict[str, str], optional): Additional HTML attributes. Defaults to None.
            
        Returns:
            Dict[str, Any]: The button configuration.
        """
        return self.ui_component_manager.create_button(label, url, variant, additional_classes, attributes)
    
    def create_cta(self, label: str, url: str, variant: str = "primary", 
                  additional_classes: str = "", attributes: Dict[str, str] = None) -> Dict[str, Any]:
        """
        Create a CTA (Call to Action) configuration.
        
        Args:
            label (str): The CTA label text.
            url (str): The URL the CTA links to.
            variant (str, optional): The CTA variant. Defaults to "primary".
            additional_classes (str, optional): Additional CSS classes. Defaults to "".
            attributes (Dict[str, str], optional): Additional HTML attributes. Defaults to None.
            
        Returns:
            Dict[str, Any]: The CTA configuration.
        """
        return self.ui_component_manager.create_cta(label, url, variant, additional_classes, attributes)
    
    def create_card(self, title: str, content: str, image_url: str = None, 
                   link_url: str = None, variant: str = "default", 
                   additional_classes: str = "") -> Dict[str, Any]:
        """
        Create a card configuration.
        
        Args:
            title (str): The card title.
            content (str): The card content text.
            image_url (str, optional): URL to the card image. Defaults to None.
            link_url (str, optional): URL the card links to. Defaults to None.
            variant (str, optional): The card variant. Defaults to "default".
            additional_classes (str, optional): Additional CSS classes. Defaults to "".
            
        Returns:
            Dict[str, Any]: The card configuration.
        """
        return self.ui_component_manager.create_card(title, content, image_url, link_url, variant, additional_classes)
    
    def get_template_components(self, template_id: str) -> Dict[str, Any]:
        """
        Get all UI components defined for a template.
        
        Args:
            template_id (str): The ID of the template.
            
        Returns:
            Dict[str, Any]: Dictionary of UI components defined for the template.
        """
        return self.ui_component_manager.get_template_components(template_id)
    
    def get_component_for_template(self, template_id: str, component_id: str) -> Optional[Dict[str, Any]]:
        """
        Get a specific UI component defined for a template.
        
        Args:
            template_id (str): The ID of the template.
            component_id (str): The ID of the component.
            
        Returns:
            Optional[Dict[str, Any]]: The component configuration, or None if not found.
        """
        return self.ui_component_manager.get_component_for_template(template_id, component_id)
    
    # Asset Management Methods
    
    def get_template_with_assets(self, template_path: str, template_id: str = None, page: str = "index", include_assets: bool = True) -> str:
        """
        Get template content with assets injected.
        
        Args:
            template_path (str): The path to the template file.
            template_id (str, optional): The ID of the template for asset collection.
            page (str, optional): The page type for section variants. Defaults to "index".
            include_assets (bool, optional): Whether to include assets. Defaults to True.
            
        Returns:
            str: The template content with assets injected.
        """
        # Get base template content
        template_content = self.get_template_content(template_path)
        
        if not include_assets or not template_id:
            return template_content
        
        # Get section variants for the template and page
        section_variants = self.get_section_variants(template_id, page)
        if not section_variants:
            return template_content
        
        # Collect assets for the section variants
        assets = self.asset_manager.collect_assets_for_template(template_id, section_variants)
        
        # Generate HTML for assets
        css_html = self.asset_manager.generate_css_html(assets.get('css', []))
        js_html = self.asset_manager.generate_js_html(assets.get('js', []))
        
        # Inject assets into template
        # Replace placeholder tags in the template
        template_content = template_content.replace('{{ injected_css_assets }}', css_html)
        template_content = template_content.replace('{{ injected_js_assets }}', js_html)
        
        return template_content
    
    def get_assets_for_template(self, template_id: str, page: str = "index") -> Dict[str, List[str]]:
        """
        Get all assets required for a template and page.
        
        Args:
            template_id (str): The ID of the template.
            page (str, optional): The page type. Defaults to "index".
            
        Returns:
            Dict[str, List[str]]: Dictionary with 'css' and 'js' keys containing asset paths.
        """
        section_variants = self.get_section_variants(template_id, page)
        if not section_variants:
            return {"css": [], "js": []}
        
        return self.asset_manager.collect_assets_for_template(template_id, section_variants)
    
    def get_available_assets(self, section_name: str, variant: str) -> Dict[str, List[str]]:
        """
        Get available assets for a specific section variant.
        
        Args:
            section_name (str): The name of the section.
            variant (str): The variant ID.
            
        Returns:
            Dict[str, List[str]]: Dictionary with 'css' and 'js' keys containing asset paths.
        """
        return self.asset_manager.discover_section_assets(section_name, variant)
    
    def validate_template_assets(self, template_id: str, page: str = "index") -> Dict[str, Any]:
        """
        Validate that all required assets exist for a template.
        
        Args:
            template_id (str): The ID of the template.
            page (str, optional): The page type. Defaults to "index".
            
        Returns:
            Dict[str, Any]: Validation results with missing assets and status.
        """
        assets = self.get_assets_for_template(template_id, page)
        missing = self.asset_manager.validate_assets(assets)
        
        has_missing = bool(missing.get('css') or missing.get('js'))
        
        return {
            "valid": not has_missing,
            "assets": assets,
            "missing": missing,
            "template_id": template_id,
            "page": page
        }
    
    def get_asset_content(self, asset_path: str) -> Optional[str]:
        """
        Get the content of an asset file.
        
        Args:
            asset_path (str): The path to the asset file.
            
        Returns:
            Optional[str]: The content of the asset file, or None if not found.
        """
        return self.asset_manager.get_asset_content(asset_path)
    
    def generate_asset_html(self, template_id: str, page: str = "index", inline: bool = True) -> Dict[str, str]:
        """
        Generate HTML for template assets.
        
        Args:
            template_id (str): The ID of the template.
            page (str, optional): The page type. Defaults to "index".
            inline (bool, optional): Whether to inline assets or use external links. Defaults to True.
            
        Returns:
            Dict[str, str]: Dictionary with 'css' and 'js' keys containing HTML strings.
        """
        assets = self.get_assets_for_template(template_id, page)
        
        return {
            "css": self.asset_manager.generate_css_html(assets.get('css', []), inline),
            "js": self.asset_manager.generate_js_html(assets.get('js', []), inline)
        }
    
    def render_template_with_assets(self, master_json: dict, template_id: str, section_variants: dict = None, skip_version: bool = False, page: str = None) -> str:
        """
        Render a complete HTML landing page from master JSON with assets included.

        Args:
            master_json (dict): The master JSON data.
            template_id (str): The ID of the template.
            section_variants (dict, optional): Custom section variants to use.
            skip_version (bool): Whether to skip version selection and use v1.
            page (str, optional): The page slug to render (e.g. "index", "shop").

        Returns:
            str: The rendered HTML with assets injected.

        Raises:
            ValueError: If rendering fails or page not defined.
        """
        if self.jinja_env is None:
            raise ValueError("Jinja2 is required for template rendering. Please install jinja2: pip install jinja2")

        try:
            meta = master_json.get("settings", {})
            sections = master_json.get("sections", {})

            # Load template configuration using the template manager
            template_config = self.registry.get_template_config(template_id)
            if not template_config:
                raise ValueError(f"Template '{template_id}' not found in registry")

            # Determine layout path and section list based on page slug
            if page:
                # Get page configuration from asset-registry.json
                asset_registry = self.asset_manager.get_asset_registry()
                if template_id in asset_registry.get("templates", {}):
                    template_assets = asset_registry["templates"][template_id]
                    if "pages" in template_assets and page in template_assets["pages"]:
                        page_conf = template_assets["pages"][page]
                        layout_path = page_conf["template_path"]
                        sections_list = page_conf["sections"]
                    else:
                        raise ValueError(f"Page '{page}' not defined for template '{template_id}' in asset-registry")
                else:
                    raise ValueError(f"Template '{template_id}' not found in asset-registry")
            else:
                # Fallback to single-page layout from asset-registry.json
                asset_registry = self.asset_manager.get_asset_registry()
                if template_id in asset_registry.get("templates", {}):
                    template_assets = asset_registry["templates"][template_id]
                    if "pages" in template_assets and "index" in template_assets["pages"]:
                        page_conf = template_assets["pages"]["index"]
                        layout_path = page_conf["template_path"]
                        sections_list = page_conf["sections"]
                    else:
                        # Fallback to template registry
                        layout_path = template_config["template_path"]
                        sections_list = template_config["sections"]
                else:
                    # Fallback to template registry
                    layout_path = template_config["template_path"]
                    sections_list = template_config["sections"]

            # Get section variants for asset collection
            if not section_variants:
                section_variants = self.get_section_variants(template_id, page or "index")

            # Collect assets for the section variants
            assets = self.asset_manager.collect_assets_for_template(template_id, section_variants)
            
            # Generate HTML for dependencies
            dependencies_css_html = self.asset_manager.get_dependencies_html(template_id, "css")
            dependencies_js_html = self.asset_manager.get_dependencies_html(template_id, "js")
            
            # Generate HTML for assets
            css_html = self.asset_manager.generate_css_html(assets.get('css', []))
            js_html = self.asset_manager.generate_js_html(assets.get('js', []))
            
            # Generate Tailwind configuration
            tailwind_config = self.asset_manager.generate_tailwind_config(meta)

            # Render each section with Jinja2
            sections_html = {}
            for section_name in sections_list:
                if section_name not in sections:
                    continue

                # Select variant
                if section_variants and section_name in section_variants:
                    variant = section_variants[section_name]
                elif not skip_version:
                    # Use the variant from section_variants or default to v1
                    variant = section_variants.get(section_name, "v1")
                else:
                    variant = "v1"

                section_path = f"templates/sections/{section_name}/{variant}.html"
                try:
                    section_template = self.jinja_env.get_template(section_path)
                except Exception as e:
                    print(f"Failed to load section template {section_path}: {e}")
                    continue

                section_data = sections.get(section_name, {})
                
                # Get navigation data for this template
                navigation_data = self.get_navigation_config(template_id) or {}
                
                # Build context for section rendering
                # Create a custom object that allows dot notation access
                class DictObj:
                    def __init__(self, d):
                        for k, v in d.items():
                            if isinstance(v, dict):
                                setattr(self, k, DictObj(v))
                            else:
                                setattr(self, k, v)
                
                section_context = {
                    'data': DictObj(section_data) if isinstance(section_data, dict) else section_data,
                    'section': DictObj(section_data) if isinstance(section_data, dict) else section_data,
                    'meta': DictObj(meta) if isinstance(meta, dict) else meta,
                    'settings': DictObj(meta) if isinstance(meta, dict) else meta,
                    'sections': DictObj(sections) if isinstance(sections, dict) else sections,
                    'navigation': DictObj(navigation_data) if isinstance(navigation_data, dict) else navigation_data,
                    'range': range,
                    'len': len,
                    'enumerate': enumerate,
                    'str': str,
                    'int': int,
                    'float': float,
                    'bool': bool,
                    'list': list,
                    'dict': dict,
                    'zip': zip,
                    'map': map,
                    'filter': filter,
                    'sorted': sorted,
                    'reversed': reversed,
                    'min': min,
                    'max': max,
                    'sum': sum,
                    'abs': abs,
                    'round': round
                }
                
                # Add items if present
                if isinstance(section_data, dict) and 'items' in section_data and isinstance(section_data['items'], list):
                    section_context['items'] = section_data['items']
                if isinstance(section_data, dict) and 'viewType' in section_data:
                    section_context['viewType'] = section_data['viewType']

                try:
                    rendered_section = section_template.render(**section_context)
                    sections_html[section_name] = rendered_section
                except Exception as e:
                    print(f"Error rendering section {section_name}: {e}")
                    sections_html[section_name] = f"<div>Error rendering {section_name}</div>"

            # Get navigation data using the new API
            navigation_data = self.get_navigation_config(template_id) or {}

            # Load and render the layout template with Jinja2
            layout_template = self.jinja_env.get_template(layout_path)
            
            # Build final context for layout rendering
            # Create a custom object that allows dot notation access
            class DictObj:
                def __init__(self, d):
                    for k, v in d.items():
                        if isinstance(v, dict):
                            setattr(self, k, DictObj(v))
                        else:
                            setattr(self, k, v)
            
            final_context = {
                'sections': sections_html,
                'meta': DictObj(meta) if isinstance(meta, dict) else meta,
                'settings': DictObj(meta) if isinstance(meta, dict) else meta,
                'registry': DictObj(self.registry.get_all_templates()) if isinstance(self.registry.get_all_templates(), dict) else self.registry.get_all_templates(),
                'page': page,
                'navigation': DictObj(navigation_data) if isinstance(navigation_data, dict) else navigation_data,
                'range': range,
                'len': len,
                'enumerate': enumerate,
                'str': str,
                'int': int,
                'float': float,
                'bool': bool,
                'list': list,
                'dict': dict,
                'zip': zip,
                'map': map,
                'filter': filter,
                'sorted': sorted,
                'reversed': reversed,
                'min': min,
                'max': max,
                'sum': sum,
                'abs': abs,
                'round': round,
                'dependencies_css': dependencies_css_html,
                'dependencies_js': dependencies_js_html,
                'injected_css_assets': css_html,
                'injected_js_assets': js_html,
                'tailwind_config': tailwind_config
            }

            # Also provide raw section data if needed
            sections_data = {}
            for section_name in sections_list:
                if section_name in sections:
                    sections_data[section_name] = sections[section_name]
            final_context['sections_data'] = sections_data

            # Render the final HTML
            final_html = layout_template.render(**final_context)
            return final_html

        except Exception as e:
            raise ValueError(f"Failed to render template {template_id}: {e}")
