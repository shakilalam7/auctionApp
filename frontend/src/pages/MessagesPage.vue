<template>
  <div class="min-h-screen bg-gradient-to-br from-slate-950 via-indigo-950 to-purple-950 relative overflow-hidden">
    <!-- Updated background to match signup page -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
      <div class="particle particle-1"></div>
      <div class="particle particle-2"></div>
      <div class="particle particle-3"></div>
    </div>

    <nav class="bg-slate-900/50 backdrop-blur-md border-b border-slate-700/50 sticky top-0 z-50 shadow-sm">
      <div class="max-w-7xl mx-auto px-6 py-4">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-8">
            <router-link to="/" class="flex items-center gap-3">
              <div class="w-10 h-10 bg-gradient-to-br from-blue-600 to-purple-600 rounded-xl flex items-center justify-center shadow-md">
                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
                </svg>
              </div>
              <div>
                <h1 class="text-xl font-bold text-white">Messages</h1>
                <p class="text-xs text-slate-400">Your conversations</p>
              </div>
            </router-link>
          </div>
          
          <!-- Changed from "/" to "/home" -->
          <router-link to="/home" class="text-sm font-medium text-purple-400 hover:text-purple-300 transition-colors">
            ← Back to Dashboard
          </router-link>
        </div>
      </div>
    </nav>
    
    <div class="max-w-6xl mx-auto px-6 py-8">
      <!-- Added empty state when no messages -->
      <div v-if="messages.length === 0" class="text-center py-20">
        <div class="w-24 h-24 bg-slate-800 rounded-full flex items-center justify-center mx-auto mb-6">
          <svg class="w-12 h-12 text-slate-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
          </svg>
        </div>
        <h3 class="text-2xl font-bold text-white mb-2">No Messages Yet</h3>
        <p class="text-slate-400 mb-6">Start a conversation with sellers or buyers</p>
        <router-link to="/browse" class="inline-flex items-center px-6 py-3 bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white rounded-xl font-semibold transition-all shadow-lg">
          Browse Auctions
        </router-link>
      </div>

      <div v-else class="grid lg:grid-cols-3 gap-6 h-[calc(100vh-200px)]">
        <!-- Conversations List -->
        <div class="bg-slate-900 rounded-2xl shadow-lg border border-slate-800 overflow-hidden">
          <div class="p-4 border-b border-slate-800">
            <input type="text" placeholder="Search messages..." class="w-full px-4 py-2 bg-slate-800 border border-slate-700 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 text-white placeholder-slate-500">
          </div>
          <div class="overflow-y-auto h-full">
            <div class="p-4 hover:bg-slate-800 cursor-pointer border-b border-slate-800 bg-blue-900/30">
              <div class="flex items-center gap-3">
                <div class="w-12 h-12 bg-gradient-to-br from-violet-500 to-purple-500 rounded-xl flex items-center justify-center text-white font-bold flex-shrink-0">
                  JS
                </div>
                <div class="flex-1 min-w-0">
                  <h4 class="font-semibold text-white truncate">John Smith</h4>
                  <p class="text-sm text-slate-400 truncate">Thanks for your interest in...</p>
                </div>
                <span class="text-xs text-slate-500">2m</span>
              </div>
            </div>
            
            <div class="p-4 hover:bg-slate-800 cursor-pointer border-b border-slate-800">
              <div class="flex items-center gap-3">
                <div class="w-12 h-12 bg-gradient-to-br from-emerald-500 to-teal-500 rounded-xl flex items-center justify-center text-white font-bold flex-shrink-0">
                  EM
                </div>
                <div class="flex-1 min-w-0">
                  <h4 class="font-semibold text-white truncate">Emma Miller</h4>
                  <p class="text-sm text-slate-400 truncate">Is the item still available?</p>
                </div>
                <span class="text-xs text-slate-500">1h</span>
              </div>
            </div>
            
            <div class="p-4 hover:bg-slate-800 cursor-pointer border-b border-slate-800">
              <div class="flex items-center gap-3">
                <div class="w-12 h-12 bg-gradient-to-br from-amber-500 to-orange-500 rounded-xl flex items-center justify-center text-white font-bold flex-shrink-0">
                  MW
                </div>
                <div class="flex-1 min-w-0">
                  <h4 class="font-semibold text-white truncate">Mike Wilson</h4>
                  <p class="text-sm text-slate-400 truncate">Great! I'll send payment today</p>
                </div>
                <span class="text-xs text-slate-500">3h</span>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Chat Area -->
        <div class="lg:col-span-2 bg-slate-900 rounded-2xl shadow-lg border border-slate-800 flex flex-col">
          <div class="p-4 border-b border-slate-800">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 bg-gradient-to-br from-violet-500 to-purple-500 rounded-xl flex items-center justify-center text-white font-bold">
                JS
              </div>
              <div>
                <h4 class="font-semibold text-white">John Smith</h4>
                <p class="text-xs text-slate-400">Active now</p>
              </div>
            </div>
          </div>
          
          <div class="flex-1 p-6 overflow-y-auto space-y-4">
            <div class="flex items-start gap-3">
              <div class="w-8 h-8 bg-gradient-to-br from-violet-500 to-purple-500 rounded-lg flex items-center justify-center text-white text-xs font-bold flex-shrink-0">
                JS
              </div>
              <div class="bg-slate-800 rounded-2xl rounded-tl-none px-4 py-3 max-w-md">
                <p class="text-sm text-white">Hi! I'm interested in the Vintage Macbook. Is it still available?</p>
                <p class="text-xs text-slate-500 mt-1">10:30 AM</p>
              </div>
            </div>
            
            <div class="flex items-start gap-3 justify-end">
              <div class="bg-gradient-to-r from-blue-600 to-purple-600 rounded-2xl rounded-tr-none px-4 py-3 max-w-md">
                <p class="text-sm text-white">Yes, it's still available! Feel free to place a bid.</p>
                <p class="text-xs text-blue-200 mt-1">10:32 AM</p>
              </div>
            </div>
            
            <div class="flex items-start gap-3">
              <div class="w-8 h-8 bg-gradient-to-br from-violet-500 to-purple-500 rounded-lg flex items-center justify-center text-white text-xs font-bold flex-shrink-0">
                JS
              </div>
              <div class="bg-slate-800 rounded-2xl rounded-tl-none px-4 py-3 max-w-md">
                <p class="text-sm text-white">Thanks for your interest in my listing!</p>
                <p class="text-xs text-slate-500 mt-1">10:35 AM</p>
              </div>
            </div>
          </div>
          
          <div class="p-4 border-t border-slate-800">
            <div class="flex items-center gap-2">
              <input type="text" placeholder="Type a message..." class="flex-1 px-4 py-3 bg-slate-800 border border-slate-700 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 text-white placeholder-slate-500">
              <button class="px-6 py-3 bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white rounded-xl font-semibold transition-all">
                Send
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue';

export default defineComponent({
  name: 'MessagesPage',
  setup() {
    const messages = ref<any[]>([]);

    onMounted(async () => {
      // Fetch messages from API when implemented
      try {
        const response = await fetch('/api/messages/', {
          credentials: 'include',
        });
        const data = await response.json();
        if (data.ok) {
          messages.value = data.messages || [];
        }
      } catch (err) {
        console.error('Failed to fetch messages:', err);
      }
    });

    return {
      messages,
    };
  },
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
