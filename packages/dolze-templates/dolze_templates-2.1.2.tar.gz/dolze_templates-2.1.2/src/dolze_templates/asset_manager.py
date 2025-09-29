"""
Asset Manager Module

This module provides functionality for managing CSS and JavaScript assets
for templates and sections, including asset discovery, dependency resolution,
and HTML injection.
"""

import json
import os
import pkgutil
from typing import Dict, Any, List, Optional, Tuple
from pathlib import Path

class AssetManager:
    """
    Class for managing CSS and JavaScript assets for templates and sections.
    
    This class handles asset discovery, dependency resolution, and HTML injection
    for dynamic loading of section-specific and global assets.
    """
    
    def __init__(self):
        """Initialize the AssetManager with empty caches."""
        self._asset_cache = {}
        self._asset_registry_cache = None
        self._discovered_assets_cache = {}
    
    def get_asset_registry(self) -> Dict[str, Any]:
        """
        Get the asset registry configuration.
        
        Returns:
            Dict[str, Any]: The asset registry configuration.
        """
        if self._asset_registry_cache is not None:
            return self._asset_registry_cache
        
        try:
            # Try to load asset registry, create default if not found
            data = pkgutil.get_data('dolze_templates', 'asset-registry.json')
            if data:
                self._asset_registry_cache = json.loads(data.decode('utf-8'))
            else:
                # Create default registry
                self._asset_registry_cache = self._create_default_asset_registry()
        except Exception:
            # Fallback to default registry
            self._asset_registry_cache = self._create_default_asset_registry()
        
        return self._asset_registry_cache
    
    def _create_default_asset_registry(self) -> Dict[str, Any]:
        """
        Create a default asset registry configuration.
        
        Returns:
            Dict[str, Any]: Default asset registry.
        """
        return {
            "global": {
                "css": [],
                "js": [],
                "dependencies": []
            },
            "sections": {},
            "dependencies": {
                "jquery": {
                    "type": "js",
                    "url": "https://code.jquery.com/jquery-3.6.0.min.js",
                    "local": "assets/dependencies/jquery.min.js"
                },
                "aos": {
                    "type": "js", 
                    "url": "https://cdn.jsdelivr.net/npm/aos@2.3.4/dist/aos.js",
                    "local": "assets/dependencies/aos.js"
                }
            },
            "loading_order": {
                "css": ["global", "template", "sections"],
                "js": ["dependencies", "global", "template", "sections"]
            }
        }
    
    def discover_section_assets(self, section_name: str, variant: str) -> Dict[str, List[str]]:
        """
        Discover CSS and JS assets for a specific section variant.
        
        Args:
            section_name (str): The name of the section (e.g., "hero", "navigation").
            variant (str): The variant ID (e.g., "v1", "v2").
            
        Returns:
            Dict[str, List[str]]: Dictionary with 'css' and 'js' keys containing asset paths.
        """
        cache_key = f"{section_name}_{variant}"
        # if cache_key in self._discovered_assets_cache:
        #     return self._discovered_assets_cache[cache_key]
        
        assets = {"css": [], "js": []}
        
        # First, check the asset registry for explicit mappings
        registry = self.get_asset_registry()
        sections_config = registry.get("sections", {})
        
        if section_name in sections_config and variant in sections_config[section_name]:
            section_assets = sections_config[section_name][variant]
            registry_css = section_assets.get("css", [])
            registry_js = section_assets.get("js", [])
            
            # Only use registry if it has actual assets defined
            if registry_css or registry_js:
                assets["css"].extend(registry_css)
                assets["js"].extend(registry_js)
            else:
                # Registry entry exists but is empty, fall back to auto-discovery
                css_path = f"templates/sections/{section_name}/{variant}.css"
                if self._asset_exists(css_path):
                    assets["css"].append(css_path)
                
                js_path = f"templates/sections/{section_name}/{variant}.js"
                if self._asset_exists(js_path):
                    assets["js"].append(js_path)
        else:
            # Auto-discovery: Check for CSS and JS files in filesystem
            css_path = f"templates/sections/{section_name}/{variant}.css"
            if self._asset_exists(css_path):
                assets["css"].append(css_path)
            
            js_path = f"templates/sections/{section_name}/{variant}.js"
            if self._asset_exists(js_path):
                assets["js"].append(js_path)
        
        # Cache the result
        self._discovered_assets_cache[cache_key] = assets
        return assets
    
    def _asset_exists(self, asset_path: str) -> bool:
        """
        Check if an asset file exists in the package.
        
        Args:
            asset_path (str): The path to the asset file.
            
        Returns:
            bool: True if the asset exists, False otherwise.
        """
        try:
            data = pkgutil.get_data('dolze_templates', asset_path)
            return data is not None
        except Exception:
            return False
    
    def collect_assets_for_template(self, template_id: str, section_variants: Dict[str, str]) -> Dict[str, List[str]]:
        """
        Collect all CSS and JS assets needed for a template with specific section variants.
        
        Args:
            template_id (str): The ID of the template.
            section_variants (Dict[str, str]): Mapping of section names to variant IDs.
            
        Returns:
            Dict[str, List[str]]: Dictionary with 'css' and 'js' keys containing all required assets.
        """
        all_assets = {"css": [], "js": []}
        
        # Get global assets first
        registry = self.get_asset_registry()
        global_assets = registry.get("global", {})
        
        all_assets["css"].extend(global_assets.get("css", []))
        all_assets["js"].extend(global_assets.get("js", []))
        
        # Collect section-specific assets
        for section_name, variant in section_variants.items():
            section_assets = self.discover_section_assets(section_name, variant)
            all_assets["css"].extend(section_assets["css"])
            all_assets["js"].extend(section_assets["js"])
        
        # Remove duplicates while preserving order
        all_assets["css"] = self._remove_duplicates(all_assets["css"])
        all_assets["js"] = self._remove_duplicates(all_assets["js"])
        
        return all_assets
    
    def _remove_duplicates(self, asset_list: List[str]) -> List[str]:
        """
        Remove duplicates from asset list while preserving order.
        
        Args:
            asset_list (List[str]): List of asset paths.
            
        Returns:
            List[str]: List with duplicates removed.
        """
        seen = set()
        result = []
        for item in asset_list:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result
    
    def get_asset_content(self, asset_path: str) -> Optional[str]:
        """
        Get the content of an asset file.
        
        Args:
            asset_path (str): The path to the asset file.
            
        Returns:
            Optional[str]: The content of the asset file, or None if not found.
        """
        if asset_path in self._asset_cache:
            return self._asset_cache[asset_path]
        
        try:
            data = pkgutil.get_data('dolze_templates', asset_path)
            if data:
                content = data.decode('utf-8')
                self._asset_cache[asset_path] = content
                return content
        except Exception:
            pass
        
        return None
    
    def generate_css_html(self, css_assets: List[str], inline: bool = True) -> str:
        """
        Generate HTML for CSS assets.
        
        Args:
            css_assets (List[str]): List of CSS asset paths.
            inline (bool): Whether to inline CSS content or use link tags.
            
        Returns:
            str: HTML string for CSS inclusion.
        """
        html_parts = []
        
        for css_path in css_assets:
            if inline:
                content = self.get_asset_content(css_path)
                if content:
                    html_parts.append(f"<style>\n{content}\n</style>")
            else:
                # For future implementation of external CSS links
                html_parts.append(f'<link rel="stylesheet" href="{css_path}">')
        
        return "\n".join(html_parts)
    
    def generate_js_html(self, js_assets: List[str], inline: bool = True) -> str:
        """
        Generate HTML for JavaScript assets.
        
        Args:
            js_assets (List[str]): List of JavaScript asset paths.
            inline (bool): Whether to inline JS content or use script tags.
            
        Returns:
            str: HTML string for JavaScript inclusion.
        """
        html_parts = []
        for js_path in js_assets:
            if inline:
                content = self.get_asset_content(js_path)
                if content:
                    html_parts.append(f"<script>\n{content}\n</script>")
            else:
                # For future implementation of external JS links
                html_parts.append(f'<script src="{js_path}"></script>')
        
        return "\n".join(html_parts)
    
    def validate_assets(self, assets: Dict[str, List[str]]) -> Dict[str, List[str]]:
        """
        Validate that all assets exist and return missing assets.
        
        Args:
            assets (Dict[str, List[str]]): Dictionary of CSS and JS assets.
            
        Returns:
            Dict[str, List[str]]: Dictionary of missing assets.
        """
        missing = {"css": [], "js": []}
        
        for asset_type, asset_list in assets.items():
            for asset_path in asset_list:
                if not self._asset_exists(asset_path):
                    missing[asset_type].append(asset_path)
        
        return missing
    
    def get_assets_for_sections(self, section_variants: Dict[str, str]) -> Dict[str, List[str]]:
        """
        Get all assets for a list of section variants.
        
        Args:
            section_variants (Dict[str, str]): Mapping of section names to variant IDs.
            
        Returns:
            Dict[str, List[str]]: Dictionary with 'css' and 'js' keys containing all assets.
        """
        all_assets = {"css": [], "js": []}
        
        for section_name, variant in section_variants.items():
            section_assets = self.discover_section_assets(section_name, variant)
            all_assets["css"].extend(section_assets["css"])
            all_assets["js"].extend(section_assets["js"])
        
        # Remove duplicates
        all_assets["css"] = self._remove_duplicates(all_assets["css"])
        all_assets["js"] = self._remove_duplicates(all_assets["js"])
        
        return all_assets
    
    def get_dependencies_html(self, template_id: str, asset_type: str = "css") -> str:
        """
        Generate HTML for dependencies based on template configuration.
        
        Args:
            template_id (str): The template ID.
            asset_type (str): Type of assets to generate ("css" or "js").
            
        Returns:
            str: HTML string for dependency inclusion.
        """
        registry = self.get_asset_registry()
        html_parts = []
        
        # Load global dependencies
        global_dependencies = registry.get("dependencies", {})
        for dep_name, dep_config in global_dependencies.items():
            dep_type = dep_config.get("type", "js")
            
            # Skip if dependency type doesn't match requested type
            if dep_type != asset_type and dep_type != "both":
                continue
            
            if asset_type == "css":
                if "css_url" in dep_config:
                    html_parts.append(f'<link rel="stylesheet" href="{dep_config["css_url"]}">')
            else:  # js
                if "js_url" in dep_config:
                    html_parts.append(f'<script src="{dep_config["js_url"]}"></script>')
        
        # Load template-specific dependencies
        templates = registry.get("templates", {})
        if template_id in templates:
            template_config = templates[template_id]
            template_dependencies = template_config.get("dependencies", [])
            
            for dep_item in template_dependencies:
                for dep_name, dep_config in dep_item.items():
                    dep_type = dep_config.get("type", "js")
                    
                    # Skip if dependency type doesn't match requested type
                    if dep_type != asset_type and dep_type != "both":
                        continue
                    
                    if asset_type == "css":
                        if "css_url" in dep_config:
                            html_parts.append(f'<link rel="stylesheet" href="{dep_config["css_url"]}">')
                    else:  # js
                        if "js_url" in dep_config:
                            html_parts.append(f'<script src="{dep_config["js_url"]}"></script>')
        
        return '\n'.join(html_parts)
    
    def generate_tailwind_config(self, settings: dict) -> str:
        """
        Generate Tailwind CSS v4 @theme configuration.
        
        Args:
            settings (dict): Settings containing theme configuration.
            
        Returns:
            str: CSS @theme block for Tailwind v4.
        """
        theme_colors = settings.get("theme", {}).get("colors", {})
        
        # Helper function to generate color palette from a base color
        def generate_color_palette(base_color: str) -> dict:
            """Generate a full color palette from a base color"""
            # Convert hex to RGB
            def hex_to_rgb(hex_color):
                hex_color = hex_color.lstrip('#')
                return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
            
            # Convert RGB to hex
            def rgb_to_hex(rgb):
                return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"
            
            # Lighten color
            def lighten_color(rgb, factor):
                return tuple(min(255, int(c + (255 - c) * factor)) for c in rgb)
            
            # Darken color
            def darken_color(rgb, factor):
                return tuple(max(0, int(c * (1 - factor))) for c in rgb)
            
            try:
                rgb = hex_to_rgb(base_color)
                return {
                    "50": rgb_to_hex(lighten_color(rgb, 0.9)),
                    "100": rgb_to_hex(lighten_color(rgb, 0.8)),
                    "200": rgb_to_hex(lighten_color(rgb, 0.6)),
                    "300": rgb_to_hex(lighten_color(rgb, 0.4)),
                    "400": rgb_to_hex(lighten_color(rgb, 0.2)),
                    "500": base_color,  # Base color
                    "600": rgb_to_hex(darken_color(rgb, 0.1)),
                    "700": rgb_to_hex(darken_color(rgb, 0.2)),
                    "800": rgb_to_hex(darken_color(rgb, 0.3)),
                    "900": rgb_to_hex(darken_color(rgb, 0.4)),
                    "950": rgb_to_hex(darken_color(rgb, 0.5)),
                }
            except:
                # Fallback to simple opacity-based approach if color parsing fails
                return {
                    "50": f"{base_color}0D",
                    "100": f"{base_color}1A",
                    "200": f"{base_color}33",
                    "300": f"{base_color}4D",
                    "400": f"{base_color}66",
                    "500": base_color,
                    "600": f"{base_color}CC",
                    "700": f"{base_color}E6",
                    "800": f"{base_color}F0",
                    "900": f"{base_color}FA",
                    "950": f"{base_color}FF",
                }
        
        # Generate color palettes
        primary_palette = generate_color_palette(theme_colors.get("primary", "#6366F1"))
        secondary_palette = generate_color_palette(theme_colors.get("secondary", "#1F2937"))
        accent_palette = generate_color_palette(theme_colors.get("accent", "#A5B4FC"))
        success_palette = generate_color_palette(theme_colors.get("success", "#10B981"))
        warning_palette = generate_color_palette(theme_colors.get("warning", "#F59E0B"))
        error_palette = generate_color_palette(theme_colors.get("error", "#EF4444"))
        info_palette = generate_color_palette(theme_colors.get("info", "#3B82F6"))
        
        # Build @theme CSS using string concatenation to avoid format issues
        theme_css = f"""<style type="text/tailwindcss">
@theme {{
  /* Base colors (without numbers) */
  --color-primary: {primary_palette["500"]};
  --color-secondary: {secondary_palette["500"]};
  --color-accent: {accent_palette["500"]};
  --color-success: {success_palette["500"]};
  --color-warning: {warning_palette["500"]};
  --color-error: {error_palette["500"]};
  --color-info: {info_palette["500"]};
  --color-background: {theme_colors.get("background", "#F9FAFB")};
  
  /* Primary color shades */
  --color-primary-50: {primary_palette["50"]};
  --color-primary-100: {primary_palette["100"]};
  --color-primary-200: {primary_palette["200"]};
  --color-primary-300: {primary_palette["300"]};
  --color-primary-400: {primary_palette["400"]};
  --color-primary-500: {primary_palette["500"]};
  --color-primary-600: {primary_palette["600"]};
  --color-primary-700: {primary_palette["700"]};
  --color-primary-800: {primary_palette["800"]};
  --color-primary-900: {primary_palette["900"]};
  --color-primary-950: {primary_palette["950"]};
  
  /* Secondary color shades */
  --color-secondary-50: {secondary_palette["50"]};
  --color-secondary-100: {secondary_palette["100"]};
  --color-secondary-200: {secondary_palette["200"]};
  --color-secondary-300: {secondary_palette["300"]};
  --color-secondary-400: {secondary_palette["400"]};
  --color-secondary-500: {secondary_palette["500"]};
  --color-secondary-600: {secondary_palette["600"]};
  --color-secondary-700: {secondary_palette["700"]};
  --color-secondary-800: {secondary_palette["800"]};
  --color-secondary-900: {secondary_palette["900"]};
  --color-secondary-950: {secondary_palette["950"]};
  
  /* Accent color shades */
  --color-accent-50: {accent_palette["50"]};
  --color-accent-100: {accent_palette["100"]};
  --color-accent-200: {accent_palette["200"]};
  --color-accent-300: {accent_palette["300"]};
  --color-accent-400: {accent_palette["400"]};
  --color-accent-500: {accent_palette["500"]};
  --color-accent-600: {accent_palette["600"]};
  --color-accent-700: {accent_palette["700"]};
  --color-accent-800: {accent_palette["800"]};
  --color-accent-900: {accent_palette["900"]};
  --color-accent-950: {accent_palette["950"]};
  
  /* Success color shades */
  --color-success-50: {success_palette["50"]};
  --color-success-100: {success_palette["100"]};
  --color-success-200: {success_palette["200"]};
  --color-success-300: {success_palette["300"]};
  --color-success-400: {success_palette["400"]};
  --color-success-500: {success_palette["500"]};
  --color-success-600: {success_palette["600"]};
  --color-success-700: {success_palette["700"]};
  --color-success-800: {success_palette["800"]};
  --color-success-900: {success_palette["900"]};
  --color-success-950: {success_palette["950"]};
  
  /* Warning color shades */
  --color-warning-50: {warning_palette["50"]};
  --color-warning-100: {warning_palette["100"]};
  --color-warning-200: {warning_palette["200"]};
  --color-warning-300: {warning_palette["300"]};
  --color-warning-400: {warning_palette["400"]};
  --color-warning-500: {warning_palette["500"]};
  --color-warning-600: {warning_palette["600"]};
  --color-warning-700: {warning_palette["700"]};
  --color-warning-800: {warning_palette["800"]};
  --color-warning-900: {warning_palette["900"]};
  --color-warning-950: {warning_palette["950"]};
  
  /* Error color shades */
  --color-error-50: {error_palette["50"]};
  --color-error-100: {error_palette["100"]};
  --color-error-200: {error_palette["200"]};
  --color-error-300: {error_palette["300"]};
  --color-error-400: {error_palette["400"]};
  --color-error-500: {error_palette["500"]};
  --color-error-600: {error_palette["600"]};
  --color-error-700: {error_palette["700"]};
  --color-error-800: {error_palette["800"]};
  --color-error-900: {error_palette["900"]};
  --color-error-950: {error_palette["950"]};
  
  /* Info color shades */
  --color-info-50: {info_palette["50"]};
  --color-info-100: {info_palette["100"]};
  --color-info-200: {info_palette["200"]};
  --color-info-300: {info_palette["300"]};
  --color-info-400: {info_palette["400"]};
  --color-info-500: {info_palette["500"]};
  --color-info-600: {info_palette["600"]};
  --color-info-700: {info_palette["700"]};
  --color-info-800: {info_palette["800"]};
  --color-info-900: {info_palette["900"]};
  --color-info-950: {info_palette["950"]};
  
  /* Font families */
  --font-family-sans: ui-sans-serif, system-ui, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  --font-family-serif: ui-serif, Georgia, Cambria, "Times New Roman", Times, serif;
  --font-family-mono: ui-monospace, SFMono-Regular, "SF Mono", Consolas, "Liberation Mono", Menlo, monospace;
  --font-family-cinzel: "Cinzel", ui-serif, Georgia, Cambria, "Times New Roman", Times, serif;
  /* Border radius values */
  --radius-none: 0px;
  --radius-sm: 4px;
  --radius: 8px;
  --radius-md: 12px;
  --radius-lg: 16px;
  --radius-xl: 20px;
  --radius-2xl: 24px;
  --radius-3xl: 32px;
  --radius-full: 9999px;
}}
</style>"""
        
        return theme_css
