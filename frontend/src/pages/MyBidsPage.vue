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
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <div>
                <h1 class="text-xl font-bold text-white">My Bids</h1>
                <p class="text-xs text-slate-400">Track your bids</p>
              </div>
            </router-link>
          </div>
          
          <router-link to="/home" class="text-sm font-medium text-purple-400 hover:text-purple-300 transition-colors">
            ← Back to Dashboard
          </router-link>
        </div>
      </div>
    </nav>
    
    <div class="max-w-7xl mx-auto px-6 py-8">
      <div v-if="loading" class="text-center py-12">
        <div class="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-purple-500"></div>
        <p class="text-slate-400 mt-4">Loading your bids...</p>
      </div>

      <div v-else-if="myBids.length === 0" class="text-center py-20">
        <div class="w-24 h-24 bg-slate-800 rounded-full flex items-center justify-center mx-auto mb-6">
          <svg class="w-12 h-12 text-slate-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
          </svg>
        </div>
        <h3 class="text-2xl font-bold text-white mb-2">No Bids Yet</h3>
        <p class="text-slate-400 mb-6">Start bidding on items you're interested in</p>
        <router-link to="/browse" class="inline-flex items-center px-6 py-3 bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white rounded-xl font-semibold transition-all shadow-lg">
          Browse Auctions
        </router-link>
      </div>

      <div v-else>
        <div class="mb-6">
          <div class="flex items-center gap-4">
            <button @click="filter = 'active'" :class="filter === 'active' ? 'bg-blue-600 text-white' : 'text-slate-400 hover:bg-slate-800'" class="px-4 py-2 rounded-lg font-medium text-sm transition-colors">
              Active ({{ activeCount }})
            </button>
            <button @click="filter = 'won'" :class="filter === 'won' ? 'bg-blue-600 text-white' : 'text-slate-400 hover:bg-slate-800'" class="px-4 py-2 rounded-lg font-medium text-sm transition-colors">
              Won ({{ wonCount }})
            </button>
            <button @click="filter = 'lost'" :class="filter === 'lost' ? 'bg-blue-600 text-white' : 'text-slate-400 hover:bg-slate-800'" class="px-4 py-2 rounded-lg font-medium text-sm transition-colors">
              Lost ({{ lostCount }})
            </button>
          </div>
        </div>
        
        <div class="space-y-4">
          <div v-for="bid in filteredBids" :key="bid.id" class="bg-slate-900 rounded-2xl p-6 shadow-lg border border-slate-800 hover:shadow-xl transition-shadow">
            <div class="flex items-center gap-6">
              <div class="w-24 h-24 bg-gradient-to-br from-slate-800 to-slate-700 rounded-xl flex items-center justify-center flex-shrink-0">
                <img v-if="bid.item.image_url" :src="bid.item.image_url" :alt="bid.item.title" class="w-full h-full object-cover rounded-xl" />
                <svg v-else class="w-12 h-12 text-slate-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
                </svg>
              </div>
              <div class="flex-1">
                <div class="flex items-start justify-between mb-2">
                  <h3 class="text-lg font-bold text-white">{{ bid.item.title }}</h3>
                  <span :class="bid.is_winning ? 'bg-emerald-100 text-emerald-700' : 'bg-red-100 text-red-700'" class="px-3 py-1 text-xs font-semibold rounded-full">
                    {{ bid.is_winning ? 'Winning' : 'Outbid' }}
                  </span>
                </div>
                <div class="grid grid-cols-3 gap-4 text-sm">
                  <div>
                    <p class="text-slate-400 mb-1">Your Bid</p>
                    <p class="font-bold text-white">${{ bid.amount }}</p>
                  </div>
                  <div>
                    <p class="text-slate-400 mb-1">Current Bid</p>
                    <p :class="bid.is_winning ? 'text-white' : 'text-red-400'" class="font-bold">${{ bid.item.current_price }}</p>
                  </div>
                  <div>
                    <p class="text-slate-400 mb-1">Total Bids</p>
                    <p class="font-semibold text-white">{{ bid.item.bid_count }}</p>
                  </div>
                </div>
              </div>
              <router-link :to="`/item/${bid.item.id}`" class="px-6 py-3 bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white rounded-xl font-semibold transition-colors">
                View Item
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
  
<script lang="ts">
import { defineComponent, ref, computed, onMounted, onActivated } from 'vue';

interface BidWithItem {
  id: number;
  amount: string;
  is_winning: boolean;
  item: {
    id: number;
    title: string;
    image_url?: string;
    current_price: string;
    bid_count: number;
    is_active: boolean;
  };
}

export default defineComponent({
  name: 'MyBidsPage',
  setup() {
    const myBids = ref<BidWithItem[]>([]);
    const loading = ref(true);
    const filter = ref<'active' | 'won' | 'lost'>('active');

    const fetchMyBids = async () => {
      loading.value = true;
      try {
        const response = await fetch('/api/bids/', {
          credentials: 'include',
        });
        const data = await response.json();
        if (data.ok) {
          myBids.value = data.bids || [];
        }
      } catch (err) {
        console.error('Failed to fetch bids:', err);
      } finally {
        loading.value = false;
      }
    };

    const filteredBids = computed(() => {
      if (filter.value === 'active') {
        return myBids.value.filter(bid => bid.item.is_active);
      } else if (filter.value === 'won') {
        return myBids.value.filter(bid => !bid.item.is_active && bid.is_winning);
      } else {
        return myBids.value.filter(bid => !bid.item.is_active && !bid.is_winning);
      }
    });

    const activeCount = computed(() => myBids.value.filter(b => b.item.is_active).length);
    const wonCount = computed(() => myBids.value.filter(b => !b.item.is_active && b.is_winning).length);
    const lostCount = computed(() => myBids.value.filter(b => !b.item.is_active && !b.is_winning).length);

    onMounted(() => {
      fetchMyBids();
    });

    onActivated(() => {
      fetchMyBids();
    });

    return {
      myBids,
      loading,
      filter,
      filteredBids,
      activeCount,
      wonCount,
      lostCount,
      fetchMyBids,
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
