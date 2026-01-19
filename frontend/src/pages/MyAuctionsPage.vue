<template>
  <div class="min-h-screen bg-gradient-to-br from-slate-950 via-indigo-950 to-purple-950 relative overflow-hidden">
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
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 013.438 0 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138 3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z" />
                </svg>
              </div>
              <div>
                <h1 class="text-xl font-bold text-white">My Auctions</h1>
                <p class="text-xs text-slate-400">Your listings</p>
              </div>
            </router-link>
          </div>
          
          <div class="flex items-center gap-3">
            <router-link to="/home" class="text-sm font-medium text-purple-400 hover:text-purple-300 transition-colors">
              ← Back
            </router-link>
            <router-link to="/create" class="px-5 py-2.5 bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white rounded-xl font-semibold text-sm transition-all shadow-lg">
              + New Auction
            </router-link>
          </div>
        </div>
      </div>
    </nav>
    
    <div class="max-w-7xl mx-auto px-6 py-8">
      <div v-if="loading" class="text-center py-12">
        <div class="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-purple-500"></div>
        <p class="text-slate-400 mt-4">Loading your auctions...</p>
      </div>

      <div v-else-if="myAuctions.length === 0" class="text-center py-20">
        <div class="w-24 h-24 bg-slate-800 rounded-full flex items-center justify-center mx-auto mb-6">
          <svg class="w-12 h-12 text-slate-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4" />
          </svg>
        </div>
        <h3 class="text-2xl font-bold text-white mb-2">No Auctions Yet</h3>
        <p class="text-slate-400 mb-6">Start selling by creating your first auction listing</p>
        <router-link to="/create" class="inline-flex items-center px-6 py-3 bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white rounded-xl font-semibold transition-all shadow-lg">
          + Create Your First Auction
        </router-link>
      </div>

      <div v-else>
        <div class="mb-6">
          <div class="flex items-center gap-4">
            <button @click="filter = 'active'" :class="filter === 'active' ? 'bg-blue-600 text-white' : 'text-slate-400 hover:bg-slate-800'" class="px-4 py-2 rounded-lg font-medium text-sm transition-colors">
              Active ({{ activeCount }})
            </button>
            <button @click="filter = 'completed'" :class="filter === 'completed' ? 'bg-blue-600 text-white' : 'text-slate-400 hover:bg-slate-800'" class="px-4 py-2 rounded-lg font-medium text-sm transition-colors">
              Completed ({{ completedCount }})
            </button>
          </div>
        </div>
        
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          <div v-for="auction in filteredAuctions" :key="auction.id" class="bg-slate-900 rounded-2xl overflow-hidden shadow-lg border border-slate-800 hover:shadow-xl transition-shadow">
            <div class="aspect-video bg-gradient-to-br from-slate-800 to-slate-700 flex items-center justify-center">
              <img v-if="auction.image_url" :src="auction.image_url" :alt="auction.title" class="w-full h-full object-cover" />
              <svg v-else class="w-16 h-16 text-slate-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
              </svg>
            </div>
            <div class="p-5">
              <div class="flex items-start justify-between mb-3">
                <h3 class="font-bold text-white">{{ auction.title }}</h3>
                <span :class="auction.is_active ? 'bg-emerald-100 text-emerald-700' : 'bg-slate-100 text-slate-700'" class="px-2 py-1 text-xs font-semibold rounded-full">
                  {{ auction.is_active ? 'Active' : 'Ended' }}
                </span>
              </div>
              <div class="space-y-2 text-sm">
                <div class="flex justify-between">
                  <span class="text-slate-400">Current Bid:</span>
                  <span class="font-bold text-white">${{ auction.current_price || auction.starting_price }}</span>
                </div>
                <div class="flex justify-between">
                  <span class="text-slate-400">Bids:</span>
                  <span class="font-semibold text-white">{{ auction.bid_count || 0 }}</span>
                </div>
              </div>
              <div class="mt-4 flex gap-2">
                <router-link :to="`/item/${auction.id}`" class="flex-1 px-4 py-2 bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white rounded-lg font-medium text-sm transition-colors text-center">
                  View
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed, onMounted } from 'vue';
import type { Item } from '../types';

export default defineComponent({
  name: 'MyAuctionsPage',
  setup() {
    const myAuctions = ref<Item[]>([]);
    const loading = ref(true);
    const filter = ref<'active' | 'completed'>('active');

    const fetchMyAuctions = async () => {
      loading.value = true;
      try {
        const response = await fetch('/api/items/?my_items=true', {
          credentials: 'include',
        });
        const data = await response.json();
        if (data.ok) {
          myAuctions.value = data.items || [];
        }
      } catch (err) {
        console.error('Failed to fetch auctions:', err);
      } finally {
        loading.value = false;
      }
    };

    const filteredAuctions = computed(() => {
      return myAuctions.value.filter(auction => 
        filter.value === 'active' ? auction.is_active : !auction.is_active
      );
    });

    const activeCount = computed(() => myAuctions.value.filter(a => a.is_active).length);
    const completedCount = computed(() => myAuctions.value.filter(a => !a.is_active).length);

    onMounted(() => {
      fetchMyAuctions();
    });

    return {
      myAuctions,
      loading,
      filter,
      filteredAuctions,
      activeCount,
      completedCount,
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
