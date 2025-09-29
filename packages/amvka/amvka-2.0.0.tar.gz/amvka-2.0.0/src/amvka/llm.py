"""
Pure LangChain LLM client - Clean, Intelligent, Universal.
Asks user for provider → key → model, then works intelligently.
"""

from typing import Optional, Dict
import os

try:
    from .langchain_llm import UniversalLLMClient
    LANGCHAIN_AVAILABLE = True
except ImportError:
    LANGCHAIN_AVAILABLE = False

from .utils import print_error, print_info, print_success, print_warning
from .environment import EnvironmentDetector


class LLMClient:
    """Pure LangChain client with intelligent setup and error handling."""
    
    def __init__(self, config_manager):
        self.config_manager = config_manager
        self.client = None
        
        if not LANGCHAIN_AVAILABLE:
            self._show_langchain_setup()
            return
        
        # Try to initialize client
        try:
            self.client = UniversalLLMClient(config_manager)
            print_success("🚀 LangChain ready - Universal AI interface active!")
        except Exception as e:
            self._handle_setup_error(e)
    
    def get_command(self, query: str, context: Dict = None) -> Optional[str]:
        """Generate command with intelligent error handling."""
        
        if not self.client:
            self._show_setup_needed()
            return None
        
        try:
            return self.client.get_command(query, context)
        
        except Exception as e:
            self._handle_runtime_error(e)
            return None
    
    def _handle_setup_error(self, error: Exception):
        """Intelligent setup error handling."""
        error_msg = str(error).lower()
        
        if "no api key" in error_msg or "api_key" in error_msg:
            self._show_api_key_setup()
        elif "quota" in error_msg or "billing" in error_msg:
            self._show_quota_issue()
        elif "model" in error_msg or "not found" in error_msg:
            self._show_model_issue()
        elif any(provider in error_msg for provider in ["openai", "gemini", "anthropic", "claude"]):
            provider = next(p for p in ["openai", "gemini", "anthropic", "claude"] if p in error_msg)
            self._show_provider_setup(provider)
        else:
            self._show_general_setup_error(error)
    
    def _handle_runtime_error(self, error: Exception):
        """Intelligent runtime error handling."""
        error_msg = str(error).lower()
        
        if "quota exceeded" in error_msg or "rate limit" in error_msg:
            self._show_quota_exceeded()
        elif "invalid api key" in error_msg or "authentication" in error_msg:
            self._show_invalid_key()
        elif "model not found" in error_msg or "does not exist" in error_msg:
            self._show_model_not_found()
        elif "network" in error_msg or "connection" in error_msg:
            self._show_network_issue()
        else:
            self._show_general_runtime_error(error)
    
    # Setup Messages
    def _show_langchain_setup(self):
        """Show LangChain installation message."""
        print_error("❌ LangChain Required")
        print_info("")
        print_info("📦 Install LangChain:")
        print_info("   pip install langchain langchain-community")
        print_info("")
        print_info("🎯 Then install your preferred provider:")
        print_info("   pip install langchain-openai       # OpenAI GPT models")
        print_info("   pip install langchain-google-genai # Google Gemini")
        print_info("   pip install langchain-anthropic    # Claude models")
        print_info("")
    
    def _show_setup_needed(self):
        """Show setup needed message."""
        print_error("❌ Setup Required")
        print_info("")
        print_info("🔧 Configure amvka:")
        print_info("   amvka config")
        print_info("")
        print_info("📋 You'll need to provide:")
        print_info("   1️⃣ Provider (openai, gemini, anthropic)")
        print_info("   2️⃣ API Key")
        print_info("   3️⃣ Model name")
        print_info("")
    
    def _show_api_key_setup(self):
        """Show API key setup message."""
        print_error("❌ API Key Missing")
        print_info("")
        print_info("🔑 Set up your API key:")
        print_info("   amvka config")
        print_info("")
        print_info("💡 Get API keys from:")
        print_info("   • OpenAI: https://platform.openai.com/api-keys")
        print_info("   • Google: https://makersuite.google.com/app/apikey")
        print_info("   • Anthropic: https://console.anthropic.com/")
        print_info("")
    
    def _show_provider_setup(self, provider: str):
        """Show provider-specific setup message."""
        print_error(f"❌ {provider.title()} Setup Required")
        print_info("")
        
        if provider == "openai":
            print_info("📦 Install OpenAI provider:")
            print_info("   pip install langchain-openai")
            print_info("")
            print_info("🔑 Get API key:")
            print_info("   https://platform.openai.com/api-keys")
            
        elif provider == "gemini":
            print_info("📦 Install Gemini provider:")
            print_info("   pip install langchain-google-genai")
            print_info("")
            print_info("🔑 Get API key:")
            print_info("   https://makersuite.google.com/app/apikey")
            
        elif provider in ["anthropic", "claude"]:
            print_info("📦 Install Anthropic provider:")
            print_info("   pip install langchain-anthropic")
            print_info("")
            print_info("🔑 Get API key:")
            print_info("   https://console.anthropic.com/")
        
        print_info("")
        print_info("🔧 Then configure:")
        print_info("   amvka config")
        print_info("")
    
    # Runtime Error Messages
    def _show_quota_exceeded(self):
        """Show quota exceeded message."""
        print_error("❌ API Quota Exceeded")
        print_info("")
        print_info("💳 Solutions:")
        print_info("   1️⃣ Check your billing: Add payment method")
        print_info("   2️⃣ Wait for quota reset (usually monthly)")
        print_info("   3️⃣ Switch to different provider: amvka config")
        print_info("")
        print_info("🔄 Try again later or reconfigure with:")
        print_info("   amvka config")
        print_info("")
    
    def _show_invalid_key(self):
        """Show invalid key message."""
        print_error("❌ Invalid API Key")
        print_info("")
        print_info("🔧 Fix your configuration:")
        print_info("   amvka config")
        print_info("")
        print_info("🔑 Make sure your key is:")
        print_info("   • Copied correctly (no extra spaces)")
        print_info("   • Still active (not revoked)")
        print_info("   • Has proper permissions")
        print_info("")
    
    def _show_model_not_found(self):
        """Show model not found message."""
        print_error("❌ Model Not Available")
        print_info("")
        print_info("🤖 Reconfigure with working model:")
        print_info("   amvka config")
        print_info("")
        print_info("💡 Popular working models:")
        print_info("   • OpenAI: gpt-3.5-turbo, gpt-4")
        print_info("   • Gemini: gemini-2.0-flash, gemini-1.5-pro")
        print_info("   • Claude: claude-3-sonnet-20240229")
        print_info("")
    
    def _show_network_issue(self):
        """Show network issue message."""
        print_error("❌ Network Connection Issue")
        print_info("")
        print_info("🌐 Check your connection and try:")
        print_info("   • Internet connection working?")
        print_info("   • Firewall blocking requests?")
        print_info("   • VPN causing issues?")
        print_info("")
        print_info("🔄 Try again in a moment...")
        print_info("")
    
    def _show_quota_issue(self):
        """Show quota setup issue."""
        print_error("❌ Quota/Billing Issue")
        print_info("")
        print_info("💳 This provider needs billing setup:")
        print_info("   1️⃣ Add payment method to your account")
        print_info("   2️⃣ Or switch to free provider")
        print_info("")
        print_info("🔧 Reconfigure:")
        print_info("   amvka config")
        print_info("")
    
    def _show_model_issue(self):
        """Show model configuration issue."""
        print_error("❌ Model Configuration Issue")
        print_info("")
        print_info("🤖 Reconfigure with correct model:")
        print_info("   amvka config")
        print_info("")
        print_info("💡 Make sure model name is exact (case-sensitive)")
        print_info("")
    
    def _show_general_setup_error(self, error):
        """Show general setup error."""
        print_error("❌ Setup Error")
        print_info("")
        print_info(f"Details: {str(error)}")
        print_info("")
        print_info("🔧 Try reconfiguring:")
        print_info("   amvka config")
        print_info("")
    
    def _show_general_runtime_error(self, error):
        """Show general runtime error."""
        print_error("❌ AI Request Failed")
        print_info("")
        print_info(f"Details: {str(error)}")
        print_info("")
        print_info("🔧 Possible solutions:")
        print_info("   1️⃣ Check configuration: amvka config")
        print_info("   2️⃣ Try different model")
        print_info("   3️⃣ Check internet connection")
        print_info("")