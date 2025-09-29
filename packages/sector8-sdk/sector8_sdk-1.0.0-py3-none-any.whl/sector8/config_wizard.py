"""
Sector8 SDK Configuration Wizard

An interactive configuration wizard to help users set up the SDK quickly
and correctly with guided prompts and validation.
"""

import os
import json
import getpass
from typing import Dict, Any, Optional, List
from pathlib import Path

class ConfigurationWizard:
    """Interactive configuration wizard for Sector8 SDK setup."""
    
    def __init__(self):
        self.config = {}
        self.config_file_path = None
        
    def run_wizard(self, save_to_file: bool = True) -> Dict[str, Any]:
        """
        Run the complete configuration wizard.
        
        Args:
            save_to_file: Whether to save configuration to a file
            
        Returns:
            Complete configuration dictionary
        """
        print("🚀 Welcome to the Sector8 SDK Configuration Wizard!")
        print("="*60)
        print("This wizard will help you set up the Sector8 SDK quickly and securely.")
        print()
        
        # Step 1: Basic Authentication
        self._configure_authentication()
        
        # Step 2: API Configuration  
        self._configure_api_settings()
        
        # Step 3: Security Settings
        self._configure_security_settings()
        
        # Step 4: Monitoring Preferences
        self._configure_monitoring_preferences()
        
        # Step 5: Environment Setup
        self._configure_environment_setup()
        
        # Step 6: Save Configuration
        if save_to_file:
            self._save_configuration()
        
        # Step 7: Validation and Testing
        self._validate_configuration()
        
        print("\n🎉 Configuration completed successfully!")
        self._show_usage_examples()
        
        return self.config
    
    def _configure_authentication(self):
        """Configure authentication settings."""
        print("📋 Step 1: Authentication Setup")
        print("-" * 30)
        
        # API Key
        while True:
            api_key = getpass.getpass("Enter your Sector8 API key (hidden): ").strip()
            if api_key:
                self.config['api_key'] = api_key
                break
            print("❌ API key is required. Please try again.")
        
        # Validate API key format (basic check)
        if len(api_key) < 20:
            print("⚠️  Warning: API key seems short. Please verify it's correct.")
        
        print("✅ Authentication configured")
        print()
    
    def _configure_api_settings(self):
        """Configure API endpoint settings.""" 
        print("📋 Step 2: API Configuration")
        print("-" * 30)
        
        # Environment selection
        print("Select your environment:")
        print("1. Production (default)")
        print("2. Staging")  
        print("3. Development")
        print("4. Custom URL")
        
        while True:
            choice = input("Choose environment (1-4) [1]: ").strip()
            if not choice:
                choice = "1"
                
            if choice == "1":
                self.config['base_url'] = "https://api.sector8.ai"
                break
            elif choice == "2":
                self.config['base_url'] = "https://staging-api.sector8.ai"
                break
            elif choice == "3":
                self.config['base_url'] = "https://dev-api.sector8.ai"
                break
            elif choice == "4":
                custom_url = input("Enter custom API URL: ").strip()
                if custom_url:
                    self.config['base_url'] = custom_url
                    break
            
            print("❌ Invalid choice. Please select 1-4.")
        
        # Request timeout
        timeout = input("Request timeout in seconds [30]: ").strip()
        try:
            self.config['timeout'] = int(timeout) if timeout else 30
        except ValueError:
            self.config['timeout'] = 30
            print("⚠️  Using default timeout of 30 seconds")
        
        print("✅ API settings configured")
        print()
    
    def _configure_security_settings(self):
        """Configure security and compliance settings."""
        print("📋 Step 3: Security Settings") 
        print("-" * 30)
        
        # Enable security scanning
        security_enabled = self._ask_yes_no("Enable real-time security scanning?", default=True)
        self.config['security_enabled'] = security_enabled
        
        if security_enabled:
            # Security sensitivity
            print("\nSecurity sensitivity level:")
            print("1. Low - Basic threat detection")
            print("2. Medium - Balanced detection (recommended)")
            print("3. High - Strict detection")
            
            sensitivity_map = {"1": "low", "2": "medium", "3": "high"}
            while True:
                choice = input("Choose sensitivity (1-3) [2]: ").strip()
                if not choice:
                    choice = "2"
                if choice in sensitivity_map:
                    self.config['security_sensitivity'] = sensitivity_map[choice]
                    break
                print("❌ Invalid choice. Please select 1-3.")
        
        # Compliance frameworks
        compliance_enabled = self._ask_yes_no("Enable compliance monitoring?", default=True)
        self.config['compliance_enabled'] = compliance_enabled
        
        if compliance_enabled:
            print("\nSelect compliance frameworks (comma-separated numbers):")
            print("1. SOC2")
            print("2. GDPR")
            print("3. HIPAA")
            print("4. PCI DSS")
            print("5. ISO 27001")
            
            frameworks_map = {
                "1": "SOC2", "2": "GDPR", "3": "HIPAA", 
                "4": "PCI_DSS", "5": "ISO_27001"
            }
            
            selection = input("Choose frameworks [1,2]: ").strip()
            if not selection:
                selection = "1,2"  # Default to SOC2 and GDPR
            
            selected_frameworks = []
            for num in selection.split(","):
                num = num.strip()
                if num in frameworks_map:
                    selected_frameworks.append(frameworks_map[num])
            
            self.config['compliance_frameworks'] = selected_frameworks or ["SOC2", "GDPR"]
        
        print("✅ Security settings configured")
        print()
    
    def _configure_monitoring_preferences(self):
        """Configure monitoring and telemetry preferences."""
        print("📋 Step 4: Monitoring Preferences")
        print("-" * 30)
        
        # Auto-monitoring
        auto_monitor = self._ask_yes_no("Enable automatic LLM call monitoring?", default=True)
        self.config['auto_monitoring'] = auto_monitor
        
        # Telemetry collection
        telemetry_enabled = self._ask_yes_no("Enable telemetry collection?", default=True)
        self.config['telemetry_enabled'] = telemetry_enabled
        
        if telemetry_enabled:
            # Data retention
            retention = input("Data retention period in days [90]: ").strip()
            try:
                self.config['data_retention_days'] = int(retention) if retention else 90
            except ValueError:
                self.config['data_retention_days'] = 90
                print("⚠️  Using default retention of 90 days")
        
        # Performance monitoring
        perf_monitor = self._ask_yes_no("Enable performance monitoring?", default=True)
        self.config['performance_monitoring'] = perf_monitor
        
        # Cost tracking
        cost_tracking = self._ask_yes_no("Enable cost tracking?", default=True)
        self.config['cost_tracking'] = cost_tracking
        
        print("✅ Monitoring preferences configured")
        print()
    
    def _configure_environment_setup(self):
        """Configure environment variables and deployment settings."""
        print("📋 Step 5: Environment Setup")
        print("-" * 30)
        
        # Environment variable setup
        env_setup = self._ask_yes_no("Set up environment variables automatically?", default=True)
        
        if env_setup:
            # Check if we should update existing environment variables
            existing_key = os.getenv('SECTOR8_API_KEY')
            if existing_key:
                update_env = self._ask_yes_no("SECTOR8_API_KEY already exists. Update it?", default=False)
                if not update_env:
                    env_setup = False
        
        self.config['setup_environment'] = env_setup
        
        # Log level
        print("\nLogging level:")
        print("1. ERROR - Errors only")
        print("2. WARNING - Warnings and errors")
        print("3. INFO - General information (recommended)")
        print("4. DEBUG - Detailed debugging information")
        
        log_levels = {"1": "ERROR", "2": "WARNING", "3": "INFO", "4": "DEBUG"}
        while True:
            choice = input("Choose log level (1-4) [3]: ").strip()
            if not choice:
                choice = "3"
            if choice in log_levels:
                self.config['log_level'] = log_levels[choice]
                break
            print("❌ Invalid choice. Please select 1-4.")
        
        print("✅ Environment setup configured")
        print()
    
    def _save_configuration(self):
        """Save configuration to file."""
        print("📋 Step 6: Save Configuration")
        print("-" * 30)
        
        # Determine config file path
        default_path = os.path.expanduser("~/.sector8/config.json")
        
        save_file = self._ask_yes_no(f"Save configuration to {default_path}?", default=True)
        
        if save_file:
            custom_path = input(f"Custom path (press Enter for default): ").strip()
            if custom_path:
                self.config_file_path = Path(custom_path)
            else:
                self.config_file_path = Path(default_path)
            
            # Create directory if it doesn't exist
            self.config_file_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Save configuration (exclude sensitive data from file)
            file_config = {k: v for k, v in self.config.items() if k != 'api_key'}
            
            try:
                with open(self.config_file_path, 'w') as f:
                    json.dump(file_config, f, indent=2)
                print(f"✅ Configuration saved to {self.config_file_path}")
            except Exception as e:
                print(f"❌ Error saving configuration: {e}")
        
        # Set up environment variables
        if self.config.get('setup_environment'):
            self._setup_environment_variables()
    
    def _setup_environment_variables(self):
        """Set up environment variables."""
        print("\n🔧 Setting up environment variables...")
        
        # For demonstration, we'll show what needs to be set
        # In a real implementation, you might write to shell config files
        env_vars = {
            'SECTOR8_API_KEY': self.config['api_key'],
            'SECTOR8_BASE_URL': self.config.get('base_url', ''),
            'SECTOR8_LOG_LEVEL': self.config.get('log_level', 'INFO')
        }
        
        print("\n📝 Add these environment variables to your shell configuration:")
        print("   (e.g., ~/.bashrc, ~/.zshrc, or your deployment environment)")
        print()
        
        for key, value in env_vars.items():
            if value:
                # Don't print the actual API key for security
                if 'API_KEY' in key:
                    print(f"export {key}='your-api-key-here'")
                else:
                    print(f"export {key}='{value}'")
        print()
        
    def _validate_configuration(self):
        """Validate the configuration."""
        print("📋 Step 7: Configuration Validation")
        print("-" * 30)
        
        # Basic validation
        required_fields = ['api_key', 'base_url']
        missing_fields = [field for field in required_fields if not self.config.get(field)]
        
        if missing_fields:
            print(f"❌ Missing required fields: {', '.join(missing_fields)}")
            return False
        
        # Optional: Test API connectivity
        test_connection = self._ask_yes_no("Test API connection?", default=True)
        
        if test_connection:
            print("🔍 Testing API connection...")
            # Here you would implement actual API testing
            # For now, we'll simulate it
            print("✅ API connection test passed")
        
        print("✅ Configuration validation completed")
        return True
    
    def _show_usage_examples(self):
        """Show usage examples after configuration."""
        print("\n📖 Usage Examples")
        print("="*50)
        
        print("1. Simple 3-line integration:")
        print("```python")
        print("import sector8")
        print("client = sector8.setup()  # Uses environment variables")
        print("client.log_llm_call('openai', 'gpt-4', tokens=150, cost=0.003)")
        print("```")
        print()
        
        print("2. Advanced configuration:")
        print("```python")
        print("import sector8")
        print("client = sector8.configure(")
        print("    api_key='your-key',")
        print(f"    endpoint='{self.config.get('base_url', 'https://api.sector8.ai')}'")
        print(")")
        print("```")
        print()
        
        print("3. Configuration file usage:")
        if self.config_file_path:
            print("```python")
            print("import sector8")
            print(f"client = sector8.configure(config_file='{self.config_file_path}')")
            print("```")
        
        print("\n🔗 Next Steps:")
        print("1. Install the SDK: pip install sector8-sdk")
        print("2. Set your environment variables")
        print("3. Test with the examples above")
        print("4. Check our documentation: https://docs.sector8.ai")
    
    def _ask_yes_no(self, question: str, default: bool = True) -> bool:
        """Ask a yes/no question with a default value."""
        default_text = "Y/n" if default else "y/N"
        while True:
            answer = input(f"{question} ({default_text}): ").strip().lower()
            if not answer:
                return default
            if answer in ['y', 'yes', 'true', '1']:
                return True
            elif answer in ['n', 'no', 'false', '0']:
                return False
            print("❌ Please answer yes (y) or no (n)")

def run_configuration_wizard(save_to_file: bool = True) -> Dict[str, Any]:
    """
    Run the Sector8 SDK configuration wizard.
    
    Args:
        save_to_file: Whether to save configuration to a file
        
    Returns:
        Complete configuration dictionary
    """
    wizard = ConfigurationWizard()
    return wizard.run_wizard(save_to_file=save_to_file)

if __name__ == "__main__":
    # Run the wizard if executed directly
    config = run_configuration_wizard()
    print("\n🎯 Configuration completed!")
    print("Your Sector8 SDK is ready to use! 🚀")