<template>
  <div class="min-h-screen bg-gradient-to-br from-slate-950 via-indigo-950 to-purple-950 relative overflow-hidden">
    <!-- Using the same navigation from HomePage -->
    <nav class="bg-slate-900/50 backdrop-blur-md border-b border-slate-700/50 sticky top-0 z-50 shadow-sm">
      <div class="max-w-7xl mx-auto px-6 py-4">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-8">
            <router-link to="/" class="flex items-center gap-3">
              <div class="w-10 h-10 bg-gradient-to-br from-blue-600 to-purple-600 rounded-xl flex items-center justify-center shadow-md">
                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
                </svg>
              </div>
              <div>
                <h1 class="text-xl font-bold text-white">AuctionHub</h1>
                <p class="text-xs text-slate-400">Settings</p>
              </div>
            </router-link>
          </div>
          
          <router-link to="/home" class="text-sm font-medium text-purple-400 hover:text-purple-300 transition-colors">
            ← Back to Dashboard
          </router-link>
        </div>
      </div>
    </nav>
    
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
      <div class="particle particle-1"></div>
      <div class="particle particle-2"></div>
      <div class="particle particle-3"></div>
    </div>

    <div class="max-w-4xl mx-auto px-6 py-8 relative">
      <div class="mb-8">
        <h2 class="text-3xl font-bold text-white mb-2">Settings</h2>
        <p class="text-slate-400">Manage your account preferences and settings</p>
      </div>
      
      <div class="space-y-6">
        <!-- Account Settings -->
        <div class="bg-slate-900 rounded-2xl p-6 shadow-lg border border-slate-800">
          <h3 class="text-xl font-bold text-white mb-6">Account Settings</h3>
          <div class="space-y-4">
            <div class="flex items-center justify-between py-3 border-b border-slate-800">
              <div>
                <h4 class="font-semibold text-white">Email Notifications</h4>
                <p class="text-sm text-slate-400">Receive updates about your auctions</p>
              </div>
              <label class="relative inline-flex items-center cursor-pointer">
                <input type="checkbox" class="sr-only peer" checked>
                <div class="w-11 h-6 bg-slate-700 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-800 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-slate-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"></div>
              </label>
            </div>
            
            <div class="flex items-center justify-between py-3 border-b border-slate-800">
              <div>
                <h4 class="font-semibold text-white">Bid Alerts</h4>
                <p class="text-sm text-slate-400">Get notified when someone outbids you</p>
              </div>
              <label class="relative inline-flex items-center cursor-pointer">
                <input type="checkbox" class="sr-only peer" checked>
                <div class="w-11 h-6 bg-slate-700 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-800 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-slate-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"></div>
              </label>
            </div>
            
            <div class="flex items-center justify-between py-3">
              <div>
                <h4 class="font-semibold text-white">Marketing Emails</h4>
                <p class="text-sm text-slate-400">Receive news and offers</p>
              </div>
              <label class="relative inline-flex items-center cursor-pointer">
                <input type="checkbox" class="sr-only peer">
                <div class="w-11 h-6 bg-slate-700 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-800 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-slate-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"></div>
              </label>
            </div>
          </div>
        </div>
        
        <!-- Privacy -->
        <div class="bg-slate-900 rounded-2xl p-6 shadow-lg border border-slate-800">
          <h3 class="text-xl font-bold text-white mb-6">Privacy</h3>
          <div class="space-y-4">
            <button class="w-full text-left px-4 py-3 hover:bg-slate-800 rounded-xl transition-colors flex items-center justify-between">
              <span class="font-medium text-white">Change Password</span>
              <svg class="w-5 h-5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
              </svg>
            </button>
            <button class="w-full text-left px-4 py-3 hover:bg-slate-800 rounded-xl transition-colors flex items-center justify-between">
              <span class="font-medium text-white">Two-Factor Authentication</span>
              <svg class="w-5 h-5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
              </svg>
            </button>
            <button class="w-full text-left px-4 py-3 hover:bg-slate-800 rounded-xl transition-colors flex items-center justify-between">
              <span class="font-medium text-white">Privacy Settings</span>
              <svg class="w-5 h-5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
              </svg>
            </button>
          </div>
        </div>
        
        <!-- Danger Zone -->
        <div class="bg-slate-900 rounded-2xl p-6 shadow-lg border border-red-900/50">
          <h3 class="text-xl font-bold text-red-400 mb-4">Danger Zone</h3>
          <button class="px-6 py-3 bg-red-600 hover:bg-red-700 text-white rounded-xl font-semibold transition-colors">
            Delete Account
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'SettingsPage',
});
</script>

<style scoped>
.particle {
  position: absolute;
  background: radial-gradient(circle, rgba(147, 51, 234, 0.6) 0%, rgba(59, 130, 246, 0.3) 50%, transparent 70%);
  border-radius: 50%;
  animation: particleFloat 20s infinite ease-in-out;
}

.particle-1 {
  width: 4px;
  height: 4px;
  top: 15%;
  left: 20%;
  animation-duration: 18s;
}

.particle-2 {
  width: 6px;
  height: 6px;
  top: 70%;
  right: 25%;
  animation-duration: 22s;
  animation-delay: 2s;
}

.particle-3 {
  width: 5px;
  height: 5px;
  top: 40%;
  right: 15%;
  animation-duration: 20s;
  animation-delay: 4s;
}

@keyframes particleFloat {
  0%, 100% {
    transform: translate(0, 0) scale(1);
    opacity: 0;
  }
  10% {
    opacity: 1;
  }
  50% {
    transform: translate(100px, -100px) scale(1.5);
    opacity: 0.8;
  }
  90% {
    opacity: 1;
  }
}
</style>
