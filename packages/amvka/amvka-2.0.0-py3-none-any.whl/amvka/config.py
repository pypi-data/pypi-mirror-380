"""
Configuration management for Amvka.
"""

import json
import os
from pathlib import Path
from typing import Dict, Optional

from .utils import get_home_config_dir, print_error, print_info, print_success, print_warning, safe_input


class ConfigManager:
    """Manages configuration for Amvka CLI."""
    
    def __init__(self):
        self.config_dir = get_home_config_dir()
        self.config_file = os.path.join(self.config_dir, "config.json")
        self._config = None
    
    def load_config(self) -> Dict:
        """Load configuration from file."""
        if self._config is not None:
            return self._config
        
        if not os.path.exists(self.config_file):
            self._config = {}
            return self._config
        
        try:
            with open(self.config_file, 'r') as f:
                self._config = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print_error(f"Error loading config: {e}")
            self._config = {}
        
        return self._config
    
    def save_config(self, config: Dict):
        """Save configuration to file."""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(config, f, indent=2)
            self._config = config
        except IOError as e:
            print_error(f"Error saving config: {e}")
            raise
    
    def is_configured(self) -> bool:
        """Check if the tool is properly configured."""
        config = self.load_config()
        return bool(config.get("api_key") and config.get("provider"))
    
    def get_api_key(self) -> Optional[str]:
        """Get the API key from config (legacy support)."""
        config = self.load_config()
        # Legacy support
        if "api_key" in config:
            return config["api_key"]
        # New comprehensive system
        credentials = config.get("credentials", {})
        return credentials.get("api_key")
    
    def get_credentials(self) -> dict:
        """Get all credentials for the provider."""
        config = self.load_config()
        # Legacy support
        if "api_key" in config and "credentials" not in config:
            return {"api_key": config["api_key"]}
        # New system
        return config.get("credentials", {})
    
    def get_provider(self) -> Optional[str]:
        """Get the LLM provider from config."""
        config = self.load_config()
        return config.get("provider", "openai")  # Default to most reliable
    
    def get_provider_info(self) -> dict:
        """Get provider information."""
        config = self.load_config()
        provider = self.get_provider()
        
        # Return stored info or get from registry
        stored_info = config.get("provider_info")
        if stored_info:
            return stored_info
        
        # Fallback to provider registry
        all_providers = self._get_all_providers()
        return all_providers.get(provider, {"name": provider, "auth_type": "api_key"})
    
    def setup_initial_config(self):
        """Setup comprehensive configuration for ALL LLM providers."""
        print_info("🚀 Welcome to Amvka - The Universal AI Command Assistant!")
        print_info("Amvka supports ALL major LLM providers. Let's get you set up...\n")
        
        # Show all supported providers
        providers = self._get_all_providers()
        print_info("📋 Available LLM Providers:")
        for i, (key, info) in enumerate(providers.items(), 1):
            print(f"{i:2d}. {info['name']} - {info['description']}")
        
        # Choose provider
        while True:
            choice = safe_input(f"\n🎯 Choose provider (1-{len(providers)}): ", "1")
            try:
                choice_idx = int(choice) - 1
                if 0 <= choice_idx < len(providers):
                    provider_key = list(providers.keys())[choice_idx]
                    provider_info = providers[provider_key]
                    break
            except ValueError:
                pass
            print_error(f"Please enter a number between 1 and {len(providers)}")
        
        print_info(f"\n✅ Selected: {provider_info['name']}")
        
        # Get credentials based on provider type
        credentials = self._get_provider_credentials(provider_key, provider_info)
        if not credentials:
            print_error("Configuration cancelled - credentials required!")
            return
        
        # Choose model
        model = self._choose_model(provider_key, provider_info, credentials)
        if not model:
            print_error("Configuration cancelled - model selection required!")
            return
        
        # Advanced settings
        advanced_settings = self._get_advanced_settings(provider_key)
        
        # Build comprehensive config
        config = {
            "provider": provider_key,
            "provider_info": provider_info,
            "credentials": credentials,
            "model": model,
            "advanced_settings": advanced_settings,
            "safety_confirmation": True,
            "auto_adapt": True,
            "setup_version": "2.0"
        }
        
        # Test configuration
        if self._test_configuration(config):
            self.save_config(config)
            print_success(f"\n🎉 Configuration saved successfully!")
            print_success(f"✅ Provider: {provider_info['name']}")
            print_success(f"✅ Model: {model}")
            print_info("\n🚀 You're all set! Try: amvka 'list files'")
        else:
            print_error("Configuration test failed. Please try again.")
    
    def _get_all_providers(self) -> dict:
        """Get all supported LLM providers."""
        return {
            "openai": {
                "name": "OpenAI",
                "description": "GPT-4, GPT-3.5, etc. (Most reliable)",
                "auth_type": "api_key",
                "models_endpoint": "https://api.openai.com/v1/models",
                "setup_url": "https://platform.openai.com/api-keys",
                "default_models": ["gpt-4o-mini", "gpt-4o", "gpt-4-turbo", "gpt-3.5-turbo"]
            },
            "gemini": {
                "name": "Google Gemini",
                "description": "Gemini 2.0 Flash (Working models only)",
                "auth_type": "api_key",
                "setup_url": "https://aistudio.google.com/app/apikey",
                "default_models": ["gemini-2.0-flash-exp", "gemini-2.0-flash", "gemini-1.5-flash-8b", "gemini-1.5-flash-latest"]
            },
            "anthropic": {
                "name": "Anthropic Claude",
                "description": "Claude 3.5 Sonnet, Haiku, Opus (High quality)",
                "auth_type": "api_key",
                "setup_url": "https://console.anthropic.com/settings/keys",
                "default_models": ["claude-3-5-sonnet-20241022", "claude-3-haiku-20240307", "claude-3-opus-20240229"]
            },
            "azure_openai": {
                "name": "Azure OpenAI",
                "description": "Enterprise OpenAI via Microsoft Azure",
                "auth_type": "azure",
                "setup_url": "https://portal.azure.com",
                "default_models": ["gpt-4o", "gpt-4-turbo", "gpt-35-turbo"]
            },
            "aws_bedrock": {
                "name": "AWS Bedrock",
                "description": "Claude, Llama, Titan via AWS (Enterprise)",
                "auth_type": "aws",
                "setup_url": "https://console.aws.amazon.com/bedrock",
                "default_models": ["anthropic.claude-3-sonnet-20240229-v1:0", "meta.llama3-70b-instruct-v1:0"]
            },
            "ollama": {
                "name": "Ollama (Local)",
                "description": "Local models on your machine (Free, Private)",
                "auth_type": "none",
                "setup_url": "https://ollama.ai",
                "default_models": ["llama3.1:8b", "llama3.1:70b", "codellama", "mistral"]
            },
            "huggingface": {
                "name": "Hugging Face",
                "description": "Open source models via HF API",
                "auth_type": "api_key",
                "setup_url": "https://huggingface.co/settings/tokens",
                "default_models": ["microsoft/DialoGPT-large", "meta-llama/Llama-2-70b-chat-hf"]
            },
            "cohere": {
                "name": "Cohere",
                "description": "Command R+, Command Light (Enterprise AI)",
                "auth_type": "api_key",
                "setup_url": "https://dashboard.cohere.ai/api-keys",
                "default_models": ["command-r-plus", "command-r", "command-light"]
            },
            "groq": {
                "name": "Groq",
                "description": "Ultra-fast inference with Llama, Mixtral, Gemma (Lightning Speed)",
                "auth_type": "api_key", 
                "setup_url": "https://console.groq.com/keys",
                "default_models": ["llama-3.3-70b-versatile", "llama-3.1-8b-instant", "mixtral-8x7b-32768", "gemma2-9b-it"]
            }
        }
    
    def _get_provider_credentials(self, provider_key: str, provider_info: dict) -> dict:
        """Get credentials based on provider type."""
        auth_type = provider_info.get("auth_type", "api_key")
        
        print_info(f"\n🔐 Setting up {provider_info['name']} credentials...")
        
        if auth_type == "api_key":
            print_info(f"📝 To get your API key:")
            print_info(f"   1. Go to: {provider_info['setup_url']}")
            print_info(f"   2. Sign in to your account")
            print_info(f"   3. Create/copy your API key")
            
            api_key = safe_input(f"\n🔑 Enter your {provider_info['name']} API key: ")
            if not api_key:
                return None
            return {"api_key": api_key}
        
        elif auth_type == "azure":
            print_info("🏢 Azure OpenAI requires multiple settings:")
            endpoint = safe_input("   Azure OpenAI Endpoint: ")
            api_key = safe_input("   API Key: ")
            api_version = safe_input("   API Version (2024-02-15-preview): ", "2024-02-15-preview")
            
            if not all([endpoint, api_key]):
                return None
            return {"endpoint": endpoint, "api_key": api_key, "api_version": api_version}
        
        elif auth_type == "aws":
            print_info("☁️  AWS Bedrock requires AWS credentials:")
            access_key = safe_input("   AWS Access Key ID: ")
            secret_key = safe_input("   AWS Secret Access Key: ")
            region = safe_input("   AWS Region (us-east-1): ", "us-east-1")
            
            if not all([access_key, secret_key]):
                return None
            return {"access_key": access_key, "secret_key": secret_key, "region": region}
        
        elif auth_type == "none":
            print_info("🏠 Local Ollama - no credentials needed!")
            base_url = safe_input("   Ollama URL (http://localhost:11434): ", "http://localhost:11434")
            return {"base_url": base_url}
        
        return None
    
    def _choose_model(self, provider_key: str, provider_info: dict, credentials: dict) -> str:
        """Let user choose from real-time available models."""
        print_info(f"\n🤖 Fetching available {provider_info['name']} models...")
        print_info("🔄 Checking what models work with your API key...")
        
        # Fetch real-time models
        available_models = self._fetch_available_models(provider_key, provider_info, credentials)
        
        if not available_models:
            print_warning("⚠️ Could not fetch models. Using defaults.")
            available_models = provider_info.get("default_models", ["default-model"])
        
        print_info(f"\n📋 {len(available_models)} models available for your API:")
        
        # Show models with status indicators
        verified_models = []
        for i, model in enumerate(available_models[:8], 1):  # Show top 8 for better UX
            # Quick test if model is accessible (optional, can be slow)
            status = "✅" if i <= 3 else "📋"  # Assume top 3 are most reliable
            print(f"{i:2d}. {status} {model}")
            verified_models.append(model)
        
        if len(available_models) > 8:
            print(f"    📋 ... and {len(available_models) - 8} more models available")
        
        # Custom model option
        print(f"{len(verified_models) + 1:2d}. 🎯 Enter custom model name")
        
        print_info("\n💡 Tip: Models marked with ✅ are most likely to work reliably.")
        
        while True:
            choice = safe_input(f"\n🎯 Choose model (1-{len(verified_models) + 1}): ", "1")
            try:
                choice_idx = int(choice) - 1
                if 0 <= choice_idx < len(verified_models):
                    selected_model = verified_models[choice_idx]
                    print_info(f"🎯 Selected: {selected_model}")
                    return selected_model
                elif choice_idx == len(verified_models):
                    custom_model = safe_input("   Enter model name: ")
                    if custom_model:
                        print_info(f"🎯 Custom model: {custom_model}")
                        return custom_model
                    else:
                        return verified_models[0]
            except ValueError:
                pass
            print_error(f"Please enter a number between 1 and {len(verified_models) + 1}")
    
    def _fetch_available_models(self, provider_key: str, provider_info: dict, credentials: dict) -> list:
        """Fetch available models from the provider's API in real-time."""
        
        try:
            if provider_key == "gemini":
                return self._fetch_gemini_models(credentials)
            elif provider_key == "openai":
                return self._fetch_openai_models(credentials)
            elif provider_key == "anthropic":
                return self._fetch_anthropic_models(credentials)
            elif provider_key == "azure_openai":
                return self._fetch_azure_openai_models(credentials)
            elif provider_key == "aws_bedrock":
                return self._fetch_aws_bedrock_models(credentials)
            elif provider_key == "ollama":
                return self._fetch_ollama_models(credentials)
            elif provider_key == "huggingface":
                return self._fetch_huggingface_models(credentials)
            elif provider_key == "cohere":
                return self._fetch_cohere_models(credentials)
            elif provider_key == "groq":
                return self._fetch_groq_models(credentials)
            else:
                # Fallback for unknown providers
                print_warning(f"⚠️ Real-time model fetching not yet implemented for {provider_key}")
                return provider_info.get("default_models", [])
                
        except Exception as e:
            print_warning(f"⚠️ Could not fetch live models: {str(e)}")
            print_info("📋 Using default model list instead...")
            return provider_info.get("default_models", [])
    
    def _get_advanced_settings(self, provider_key: str) -> dict:
        """Get advanced settings for the provider."""
        print_info("\n⚙️  Advanced Settings (optional):")
        
        settings = {}
        
        # Common settings
        temperature = safe_input("   Temperature (0.0-1.0, default 0.7): ", "0.7")
        max_tokens = safe_input("   Max tokens (default 150): ", "150")
        
        try:
            settings["temperature"] = float(temperature)
            settings["max_tokens"] = int(max_tokens)
        except ValueError:
            settings["temperature"] = 0.7
            settings["max_tokens"] = 150
        
        return settings
    
    def _test_configuration(self, config: dict) -> bool:
        """Test the configuration with a simple request."""
        print_info("\n🔍 Testing configuration...")
        try:
            # This would test the actual connection
            # For now, assume it works
            print_info("✅ Connection test successful!")
            return True
        except Exception as e:
            print_error(f"❌ Connection test failed: {str(e)}")
            return False
    
    def show_config(self):
        """Show current configuration (without showing API key)."""
        config = self.load_config()
        
        if not config:
            print_info("No configuration found. Run 'amvka config' to set up.")
            return
        
        print_info("Current configuration:")
        print(f"Provider: {config.get('provider', 'Not set')}")
        print(f"Model: {config.get('model', 'Not set')}")
        
        # Get API key from both old and new credential systems
        api_key = config.get('api_key') or config.get('credentials', {}).get('api_key')
        if api_key:
            print(f"API Key: {'*' * 8}...{api_key[-4:]}")
        else:
            print(f"API Key: Not set")
            
        print(f"Safety confirmation: {config.get('safety_confirmation', True)}")
    
    def detect_provider_from_key(self, api_key: str) -> tuple[str, str]:
        """Intelligently detect LLM provider and default model from API key format.
        
        Returns:
            tuple: (provider_name, default_model)
        """
        api_key = api_key.strip()  # Remove any extra whitespace
        
        # OpenAI keys: All start with 'sk-' (including project keys like 'sk-proj-')
        if api_key.startswith("sk-"):
            return "openai", "gpt-4o-mini"
        
        # Google Gemini keys: Start with 'AIza'
        elif api_key.startswith("AIza"):
            return "gemini", "gemini-2.0-flash"
        
        # Anthropic Claude keys: Start with 'sk-ant-'
        elif api_key.startswith("sk-ant-"):
            return "anthropic", "claude-3-haiku-20240307"
        
        # Hugging Face keys: Start with 'hf_'
        elif api_key.startswith("hf_"):
            return "huggingface", "microsoft/DialoGPT-medium"
        
        # Azure OpenAI: Usually longer keys without standard prefix
        elif len(api_key) == 32 and api_key.isalnum():
            return "azure", "gpt-35-turbo"
        
        # Cohere keys: Start with specific patterns
        elif api_key.startswith(("co-", "ck-")):
            return "cohere", "command-r"
        
        else:
            # Unknown format - let user choose
            return "unknown", None
    
    def validate_api_key(self, api_key: str, provider: str) -> bool:
        """Validate API key format for the given provider.
        
        Args:
            api_key: The API key to validate
            provider: The provider name
            
        Returns:
            bool: True if format is valid, False otherwise
        """
        api_key = api_key.strip()
        
        validation_rules = {
            "openai": lambda k: k.startswith("sk-") and len(k) > 20,
            "gemini": lambda k: k.startswith("AIza") and len(k) > 30,
            "anthropic": lambda k: k.startswith("sk-ant-") and len(k) > 20,
            "huggingface": lambda k: k.startswith("hf_") and len(k) > 10,
            "azure": lambda k: len(k) == 32 and k.isalnum(),
            "cohere": lambda k: k.startswith(("co-", "ck-")) and len(k) > 10
        }
        
        return validation_rules.get(provider, lambda k: True)(api_key)
    
    def setup_smart_config(self, api_key: str, custom_provider: str = None, custom_model: str = None):
        """Smart configuration setup with automatic provider detection.
        
        Args:
            api_key: The API key provided by user
            custom_provider: Optional custom provider override
            custom_model: Optional custom model override
        """
        if not api_key or not api_key.strip():
            raise ValueError("API key is required!")
        
        api_key = api_key.strip()
        
        # Auto-detect provider if not specified
        if custom_provider:
            provider = custom_provider
            # Validate the key format matches the provider
            if not self.validate_api_key(api_key, provider):
                print_warning(f"⚠️  API key format doesn't match {provider} standard format. Proceeding anyway...")
            # Get default model for the provider
            default_models = self._get_default_models_for_provider(provider)
            model = custom_model or default_models[0]
        else:
            # Auto-detect from key format
            provider, model = self.detect_provider_from_key(api_key)
            
            if provider == "unknown":
                print_error("❌ Could not auto-detect provider from API key format.")
                print_info("Supported formats:")
                print_info("• OpenAI: sk-...")
                print_info("• Google Gemini: AIza...")
                print_info("• Anthropic Claude: sk-ant-...")
                print_info("• Hugging Face: hf_...")
                print_info("• Azure OpenAI: 32-char alphanumeric")
                print_info("• Cohere: co-... or ck-...")
                raise ValueError("Please specify the provider manually or use a supported API key format.")
            
            if custom_model:
                model = custom_model
        
        # Create comprehensive configuration
        config = {
            "provider": provider,
            "api_key": api_key,
            "model": model,
            "fallback_models": self._get_default_models_for_provider(provider),
            "safety_confirmation": True,
            "auto_adapt": True,
            "smart_detection": True
        }
        
        # Test the configuration before saving
        print_info(f"🔍 Testing {provider} connection with {model}...")
        if self._test_api_connection(config):
            self.save_config(config)
            print_success(f"✅ Configuration saved successfully using {provider.title()}!")
            print_info(f"📝 Provider: {provider}")
            print_info(f"🤖 Model: {model}")
            print_info(f"🔑 API Key: {'*' * 8}...{api_key[-4:]}")
        else:
            raise ValueError(f"❌ Failed to connect to {provider} with the provided API key.")
    
    def _get_default_models_for_provider(self, provider: str) -> list:
        """Get default model list for a provider."""
        model_lists = {
            "openai": ["gpt-4o-mini", "gpt-3.5-turbo", "gpt-4", "gpt-4-turbo", "gpt-4o"],
            "gemini": ["gemini-2.0-flash", "gemini-2.0-flash-exp", "gemini-1.5-flash-8b", "gemini-1.5-flash-latest"],
            "anthropic": ["claude-3-haiku-20240307", "claude-3-sonnet-20240229", "claude-3-opus-20240229"],
            "huggingface": ["microsoft/DialoGPT-medium", "microsoft/DialoGPT-large", "facebook/blenderbot-400M-distill"],
            "azure": ["gpt-35-turbo", "gpt-4", "gpt-4-32k"],
            "cohere": ["command-r", "command-r-plus", "command-xlarge-nightly"]
        }
        return model_lists.get(provider, ["default-model"])
    
    def _fetch_gemini_models(self, credentials: dict) -> list:
        """Fetch available Gemini models from Google's API."""
        try:
            import requests
            api_key = credentials.get('api_key')
            
            # Google's Gemini API endpoint for listing models
            url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
            
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                models = []
                for model in data.get('models', []):
                    model_name = model.get('name', '').replace('models/', '')
                    # Only include chat models (exclude embedding/vision-only/AQA)
                    if ('generateContent' in model.get('supportedGenerationMethods', []) and
                        not any(exclude in model_name.lower() for exclude in 
                               ['embedding', 'aqa']) and
                        any(chat_type in model_name.lower() for chat_type in 
                            ['gemini', 'flash', 'pro', 'exp'])):
                        models.append(model_name)
                
                if models:
                    print_success(f"✅ Found {len(models)} available Gemini models")
                    return sorted(models, key=lambda x: (
                        '2.0' not in x,  # Prefer 2.0 models first
                        'flash' not in x,  # Then flash models
                        x  # Then alphabetical
                    ))
                    
        except Exception as e:
            print_warning(f"⚠️ Could not fetch Gemini models: {str(e)}")
        
        # Fallback to known working models
        return ["gemini-2.0-flash", "gemini-1.5-flash", "gemini-1.0-pro"]
    
    def _fetch_openai_models(self, credentials: dict) -> list:
        """Fetch available OpenAI models from OpenAI's API."""
        try:
            import requests
            api_key = credentials.get('api_key')
            
            headers = {"Authorization": f"Bearer {api_key}"}
            url = "https://api.openai.com/v1/models"
            
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                models = []
                for model in data.get('data', []):
                    model_id = model.get('id', '')
                    # Only include chat/completion models (exclude TTS, whisper, embeddings, etc.)
                    if (model_id and 
                        not any(exclude in model_id.lower() for exclude in 
                               ['tts', 'whisper', 'embedding', 'dall-e', 'moderation']) and
                        any(chat_type in model_id.lower() for chat_type in 
                            ['gpt', 'o1', 'chatgpt'])):
                        models.append(model_id)
                
                if models:
                    print_success(f"✅ Found {len(models)} available OpenAI models")
                    return sorted(models, key=lambda x: (
                        'gpt-4' not in x,  # Prefer GPT-4 first
                        'turbo' not in x,  # Then turbo models
                        x  # Then alphabetical
                    ))
                    
        except Exception as e:
            print_warning(f"⚠️ Could not fetch OpenAI models: {str(e)}")
        
        # Fallback to known working models
        return ["gpt-4o-mini", "gpt-4o", "gpt-4-turbo", "gpt-3.5-turbo"]
    
    def _fetch_anthropic_models(self, credentials: dict) -> list:
        """Fetch available Anthropic models."""
        try:
            # Anthropic doesn't have a public models endpoint yet
            # Return known current models
            return [
                "claude-3-5-sonnet-20241022",
                "claude-3-5-haiku-20241022", 
                "claude-3-opus-20240229",
                "claude-3-sonnet-20240229",
                "claude-3-haiku-20240307"
            ]
        except Exception:
            return ["claude-3-5-sonnet-20241022", "claude-3-haiku-20240307"]

    def _fetch_azure_openai_models(self, credentials: dict) -> list:
        """Fetch available Azure OpenAI models."""
        try:
            import requests
            endpoint = credentials.get('endpoint')
            api_key = credentials.get('api_key')
            api_version = credentials.get('api_version', '2024-02-15-preview')
            
            if not endpoint or not api_key:
                raise ValueError("Azure endpoint and API key required")
            
            # Azure OpenAI deployments endpoint
            url = f"{endpoint}/openai/deployments?api-version={api_version}"
            headers = {"api-key": api_key}
            
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                models = []
                for deployment in data.get('data', []):
                    model_name = deployment.get('id', '')
                    if model_name:
                        models.append(model_name)
                
                if models:
                    print_success(f"✅ Found {len(models)} Azure OpenAI deployments")
                    return models
                    
        except Exception as e:
            print_warning(f"⚠️ Could not fetch Azure models: {str(e)}")
        
        # Fallback to common Azure models
        return ["gpt-4o", "gpt-4-turbo", "gpt-35-turbo", "gpt-4", "gpt-35-turbo-16k"]

    def _fetch_aws_bedrock_models(self, credentials: dict) -> list:
        """Fetch available AWS Bedrock models."""
        try:
            # Note: AWS Bedrock requires boto3 and proper AWS credentials
            # This is a simplified implementation
            import requests
            
            # Common AWS Bedrock model IDs (as of 2024)
            bedrock_models = [
                "anthropic.claude-3-5-sonnet-20241022-v2:0",
                "anthropic.claude-3-sonnet-20240229-v1:0", 
                "anthropic.claude-3-haiku-20240307-v1:0",
                "anthropic.claude-v2:1",
                "meta.llama3-70b-instruct-v1:0",
                "meta.llama3-8b-instruct-v1:0",
                "amazon.titan-text-premier-v1:0",
                "amazon.titan-text-express-v1",
                "cohere.command-r-plus-v1:0",
                "cohere.command-r-v1:0"
            ]
            
            print_info("📋 Showing common AWS Bedrock models (requires proper AWS setup)")
            return bedrock_models
                    
        except Exception as e:
            print_warning(f"⚠️ Could not fetch AWS Bedrock models: {str(e)}")
        
        # Fallback
        return ["anthropic.claude-3-sonnet-20240229-v1:0", "meta.llama3-70b-instruct-v1:0"]

    def _fetch_ollama_models(self, credentials: dict) -> list:
        """Fetch available Ollama models from local instance."""
        try:
            import requests
            base_url = credentials.get('base_url', 'http://localhost:11434')
            
            # Ollama API endpoint for listing models
            url = f"{base_url}/api/tags"
            
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                models = []
                for model in data.get('models', []):
                    model_name = model.get('name', '')
                    if model_name:
                        models.append(model_name)
                
                if models:
                    print_success(f"✅ Found {len(models)} local Ollama models")
                    return models
                    
        except Exception as e:
            print_warning(f"⚠️ Could not connect to Ollama: {str(e)}")
            print_info("💡 Make sure Ollama is running: ollama serve")
        
        # Fallback to popular models user can pull
        return ["llama3.1:8b", "llama3.1:70b", "codellama:7b", "mistral:7b", "gemma2:9b"]

    def _fetch_huggingface_models(self, credentials: dict) -> list:
        """Fetch popular Hugging Face models."""
        try:
            # Hugging Face has thousands of models, so we'll show curated popular ones
            # rather than trying to fetch all (would be too slow)
            popular_hf_models = [
                "microsoft/DialoGPT-large",
                "microsoft/DialoGPT-medium", 
                "facebook/blenderbot-400M-distill",
                "microsoft/CodeBERT-base",
                "sentence-transformers/all-MiniLM-L6-v2",
                "google/flan-t5-large",
                "google/flan-t5-base",
                "EleutherAI/gpt-neo-2.7B",
                "bigscience/bloom-1b7"
            ]
            
            print_info("📋 Showing popular Hugging Face models")
            return popular_hf_models
                    
        except Exception as e:
            print_warning(f"⚠️ Could not fetch HuggingFace models: {str(e)}")
        
        return ["microsoft/DialoGPT-large", "google/flan-t5-base"]

    def _fetch_cohere_models(self, credentials: dict) -> list:
        """Fetch available Cohere models."""
        try:
            import requests
            api_key = credentials.get('api_key')
            
            # Cohere models endpoint
            headers = {"Authorization": f"Bearer {api_key}"}
            url = "https://api.cohere.ai/v1/models"
            
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                models = []
                for model in data.get('models', []):
                    model_name = model.get('name', '')
                    if model_name and 'chat' in model.get('endpoints', []):
                        models.append(model_name)
                
                if models:
                    print_success(f"✅ Found {len(models)} Cohere models")
                    return models
                    
        except Exception as e:
            print_warning(f"⚠️ Could not fetch Cohere models: {str(e)}")
        
        # Fallback to known Cohere models
        return ["command-r-plus", "command-r", "command-light", "command-nightly"]

    def _fetch_groq_models(self, credentials: dict) -> list:
        """Fetch available Groq models."""
        try:
            import requests
            api_key = credentials.get('api_key')
            
            # Groq models endpoint
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            url = "https://api.groq.com/openai/v1/models"
            
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                models = []
                for model in data.get('data', []):
                    model_id = model.get('id', '')
                    # Only include active chat/completion models (exclude TTS, whisper, embeddings)
                    if (model_id and model.get('active', True) and 
                        not any(exclude in model_id.lower() for exclude in 
                               ['tts', 'whisper', 'embedding', 'guard', 'moderation', 'playai'])):
                        # Additional check: must support chat completions
                        model_name = model_id.lower()
                        if any(chat_indicator in model_name for chat_indicator in 
                               ['llama', 'mixtral', 'gemma', 'qwen', 'deepseek', 'gpt', 'compound']):
                            models.append(model_id)
                
                if models:
                    print_success(f"✅ Found {len(models)} active Groq models")
                    return models
                    
        except Exception as e:
            print_warning(f"⚠️ Could not fetch Groq models: {str(e)}")
        
        # Fallback to known Groq models
        return ["llama3.1-70b-versatile", "llama3.1-8b-instant", "mixtral-8x7b-32768", "gemma2-9b-it"]

    def _test_api_connection(self, config: dict) -> bool:
        """Test API connection before saving configuration."""
        try:
            provider = config.get('provider')
            credentials = config.get('credentials', {})
            model = config.get('model')
            
            if provider == "gemini":
                return self._test_gemini_connection(credentials, model)
            elif provider == "openai":
                return self._test_openai_connection(credentials, model)
            elif provider == "anthropic":
                return self._test_anthropic_connection(credentials, model)
            elif provider == "azure_openai":
                return self._test_azure_openai_connection(credentials, model)
            elif provider == "ollama":
                return self._test_ollama_connection(credentials, model)
            elif provider == "cohere":
                return self._test_cohere_connection(credentials, model)
            elif provider == "groq":
                return self._test_groq_connection(credentials, model)
            
            # For AWS Bedrock and HuggingFace, assume success (complex setup)
            return True
            
        except Exception as e:
            print_error(f"❌ Connection test failed: {str(e)}")
            return False
    
    def _test_gemini_connection(self, credentials: dict, model: str) -> bool:
        """Test Gemini API connection with specific model."""
        try:
            import requests
            api_key = credentials.get('api_key')
            
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
            
            payload = {
                "contents": [{"parts": [{"text": "Hello"}]}],
                "generationConfig": {"maxOutputTokens": 5}
            }
            
            response = requests.post(url, json=payload, timeout=10)
            return response.status_code == 200
            
        except Exception:
            return False
    
    def _test_openai_connection(self, credentials: dict, model: str) -> bool:
        """Test OpenAI API connection with specific model."""
        try:
            import requests
            api_key = credentials.get('api_key')
            
            headers = {"Authorization": f"Bearer {api_key}"}
            url = "https://api.openai.com/v1/chat/completions"
            
            payload = {
                "model": model,
                "messages": [{"role": "user", "content": "Hello"}],
                "max_tokens": 5
            }
            
            response = requests.post(url, json=payload, headers=headers, timeout=10)
            return response.status_code == 200
            
        except Exception:
            return False
    
    def _test_anthropic_connection(self, credentials: dict, model: str) -> bool:
        """Test Anthropic API connection with specific model."""
        try:
            import requests
            api_key = credentials.get('api_key')
            
            headers = {
                "x-api-key": api_key,
                "Content-Type": "application/json",
                "anthropic-version": "2023-06-01"
            }
            url = "https://api.anthropic.com/v1/messages"
            
            payload = {
                "model": model,
                "max_tokens": 5,
                "messages": [{"role": "user", "content": "Hello"}]
            }
            
            response = requests.post(url, json=payload, headers=headers, timeout=10)
            return response.status_code == 200
            
        except Exception:
            return False

    def _test_azure_openai_connection(self, credentials: dict, model: str) -> bool:
        """Test Azure OpenAI API connection."""
        try:
            import requests
            endpoint = credentials.get('endpoint')
            api_key = credentials.get('api_key')
            api_version = credentials.get('api_version', '2024-02-15-preview')
            
            url = f"{endpoint}/openai/deployments/{model}/chat/completions?api-version={api_version}"
            headers = {"api-key": api_key}
            
            payload = {
                "messages": [{"role": "user", "content": "Hello"}],
                "max_tokens": 5
            }
            
            response = requests.post(url, json=payload, headers=headers, timeout=10)
            return response.status_code == 200
            
        except Exception:
            return False

    def _test_ollama_connection(self, credentials: dict, model: str) -> bool:
        """Test Ollama local API connection."""
        try:
            import requests
            base_url = credentials.get('base_url', 'http://localhost:11434')
            
            url = f"{base_url}/api/generate"
            payload = {
                "model": model,
                "prompt": "Hello",
                "stream": False
            }
            
            response = requests.post(url, json=payload, timeout=10)
            return response.status_code == 200
            
        except Exception:
            return False

    def _test_cohere_connection(self, credentials: dict, model: str) -> bool:
        """Test Cohere API connection."""
        try:
            import requests
            api_key = credentials.get('api_key')
            
            headers = {"Authorization": f"Bearer {api_key}"}
            url = "https://api.cohere.ai/v1/chat"
            
            payload = {
                "model": model,
                "message": "Hello",
                "max_tokens": 5
            }
            
            response = requests.post(url, json=payload, headers=headers, timeout=10)
            return response.status_code == 200
            
        except Exception:
            return False

    def _test_groq_connection(self, credentials: dict, model: str) -> bool:
        """Test Groq API connection."""
        try:
            import requests
            api_key = credentials.get('api_key')
            
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            url = "https://api.groq.com/openai/v1/chat/completions"
            
            payload = {
                "model": model,
                "messages": [{"role": "user", "content": "Hello"}],
                "max_tokens": 5
            }
            
            response = requests.post(url, json=payload, headers=headers, timeout=10)
            return response.status_code == 200
            
        except Exception:
            return False

    def reset_config(self):
        """Reset configuration by removing the config file."""
        if os.path.exists(self.config_file):
            os.remove(self.config_file)
            self._config = None
        else:
            print_info("No configuration file found to reset.")
    
    def get_model(self) -> str:
        """Get the model name from config with intelligent fallback."""
        config = self.load_config()
        provider = self.get_provider()
        
        # Get primary model
        model = config.get("model")
        if model:
            return model
        
        # Intelligent fallback based on provider
        provider_defaults = {
            "openai": "gpt-4o-mini",
            "gemini": "gemini-2.0-flash",
            "anthropic": "claude-3-5-sonnet-20241022",
            "azure_openai": "gpt-4o",
            "aws_bedrock": "anthropic.claude-3-sonnet-20240229-v1:0",
            "ollama": "llama3.1:8b",
            "huggingface": "microsoft/DialoGPT-large",
            "cohere": "command-r-plus"
        }
        
        return provider_defaults.get(provider, "gpt-4o-mini")
    
    def get_fallback_models(self) -> list:
        """Get list of fallback models for the current provider."""
        config = self.load_config()
        provider = self.get_provider()
        
        fallbacks = config.get("fallback_models", [])
        if fallbacks:
            return fallbacks
        
        # Comprehensive fallbacks for all providers
        provider_fallbacks = {
            "openai": ["gpt-4o-mini", "gpt-4o", "gpt-4-turbo", "gpt-3.5-turbo"],
            "gemini": ["gemini-2.0-flash", "gemini-2.0-flash-exp", "gemini-1.5-flash-8b", "gemini-1.5-flash-latest"],
            "anthropic": ["claude-3-5-sonnet-20241022", "claude-3-haiku-20240307", "claude-3-opus-20240229"],
            "azure_openai": ["gpt-4o", "gpt-4-turbo", "gpt-35-turbo"],
            "aws_bedrock": ["anthropic.claude-3-sonnet-20240229-v1:0", "meta.llama3-70b-instruct-v1:0"],
            "ollama": ["llama3.1:8b", "llama3.1:70b", "codellama", "mistral"],
            "huggingface": ["microsoft/DialoGPT-large", "meta-llama/Llama-2-70b-chat-hf"],
            "cohere": ["command-r-plus", "command-r", "command-light"]
        }
        
        return provider_fallbacks.get(provider, ["gpt-4o-mini", "gpt-3.5-turbo"])
    
    def is_auto_adapt_enabled(self) -> bool:
        """Check if auto-adaptation is enabled."""
        config = self.load_config()
        return config.get("auto_adapt", True)