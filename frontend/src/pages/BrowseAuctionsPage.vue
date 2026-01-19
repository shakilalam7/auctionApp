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
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 bg-gradient-to-br from-blue-600 via-purple-600 to-pink-600 rounded-xl flex items-center justify-center shadow-md">
                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                </svg>
              </div>
              <div>
                <h1 class="text-xl font-bold text-white">Browse Auctions</h1>
                <p class="text-xs text-slate-300">Find your next treasure</p>
              </div>
            </div>
          </div>
          
          <router-link to="/home" class="text-sm font-medium text-purple-400 hover:text-purple-300 transition-colors">
            ← Back to Dashboard
          </router-link>
        </div>
      </div>
    </nav>
    
    <div class="max-w-7xl mx-auto px-6 py-8">
      <div class="mb-8">
        <div class="flex items-center gap-4 mb-6">
          <input 
            v-model="searchQuery"
            @input="searchItems"
            type="text" 
            placeholder="Search auctions..." 
            class="flex-1 px-5 py-3 bg-slate-800 border border-slate-700 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 shadow-sm text-white placeholder-slate-500"
          >
          <select class="px-5 py-3 bg-slate-800 border border-slate-700 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 shadow-sm text-white">
            <option>All Categories</option>
            <option>Electronics</option>
            <option>Fashion</option>
            <option>Home & Garden</option>
            <option>Collectibles</option>
          </select>
          <select class="px-5 py-3 bg-slate-800 border border-slate-700 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 shadow-sm text-white">
            <option>Sort by: Ending Soon</option>
            <option>Sort by: Newest</option>
            <option>Sort by: Price Low to High</option>
            <option>Sort by: Price High to Low</option>
          </select>
        </div>
      </div>
      
      <div v-if="loading" class="text-center py-12">
        <div class="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-purple-500"></div>
        <p class="text-slate-400 mt-4">Loading auctions...</p>
      </div>

      <div v-else-if="items.length > 0" class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
        <div v-for="item in items" :key="item.id" class="bg-slate-900 rounded-2xl overflow-hidden shadow-lg border border-slate-800 hover:shadow-xl transition-shadow cursor-pointer">
          <div class="aspect-square bg-gradient-to-br from-slate-800 to-slate-700 flex items-center justify-center">
            <img v-if="item.image_url" :src="item.image_url" :alt="item.title" class="w-full h-full object-cover" />
            <svg v-else class="w-16 h-16 text-slate-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
            </svg>
          </div>
          <div class="p-4">
            <h3 class="font-bold text-white mb-2">{{ item.title }}</h3>
            <div class="space-y-1 text-sm mb-4">
              <div class="flex justify-between">
                <span class="text-slate-400">Current Price:</span>
                <span class="font-bold text-blue-400">${{ item.current_price }}</span>
              </div>
            </div>
            <div class="flex items-center justify-between">
              <span class="text-xs text-slate-500">{{ formatEndDate(item.ends_at) }}</span>
              <router-link :to="`/item/${item.id}`" class="px-4 py-2 bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white rounded-lg text-sm font-semibold transition-colors">
                View Details
              </router-link>
            </div>
          </div>
        </div>
      </div>

      <div v-else class="text-center py-12">
        <svg class="w-16 h-16 text-slate-600 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 00-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4" />
        </svg>
        <p class="text-slate-400 font-medium">No auctions available</p>
        <p class="text-slate-500 text-sm mt-1">Check back later for new items</p>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue';
import type { Item } from '../types.ts';

export default defineComponent({
  name: 'BrowseAuctionsPage',
  setup() {
    const items = ref<Item[]>([]);
    const loading = ref(true);
    const searchQuery = ref('');

    const fetchItems = async (query: string = '') => {
      loading.value = true;
      try {
        const url = query ? `/api/items/?q=${encodeURIComponent(query)}` : '/api/items/';
        const response = await fetch(url, {
          credentials: 'include',
        });

        if (response.ok) {
          const data = await response.json();
          items.value = data.items || [];
        }
      } catch (error) {
        console.error('Failed to fetch items:', error);
      } finally {
        loading.value = false;
      }
    };

    let searchTimeout: ReturnType<typeof setTimeout>;
    const searchItems = () => {
      clearTimeout(searchTimeout);
      searchTimeout = setTimeout(() => {
        fetchItems(searchQuery.value);
      }, 500);
    };

    const formatEndDate = (dateString: string) => {
      const date = new Date(dateString);
      const now = new Date();
      const diff = date.getTime() - now.getTime();
      const days = Math.floor(diff / (1000 * 60 * 60 * 24));
      const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      
      if (days > 0) {
        return `Ends in ${days}d ${hours}h`;
      } else if (hours > 0) {
        return `Ends in ${hours}h`;
      } else {
        return 'Ending soon';
      }
    };

    onMounted(() => {
      fetchItems();
    });

    return {
      items,
      loading,
      searchQuery,
      searchItems,
      formatEndDate,
    };
  },
});
</script>

<style scoped>
/* Particle animations matching signup page */
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
