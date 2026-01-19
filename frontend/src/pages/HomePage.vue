<template>
  <div class="min-h-screen bg-gradient-to-br from-slate-950 via-indigo-950 to-purple-950 relative overflow-hidden">
    <!-- Animated gradient orbs -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
      <div class="animated-orb orb-1"></div>
      <div class="animated-orb orb-2"></div>
      <div class="animated-orb orb-3"></div>
    </div>

    <!-- Floating particles -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
      <div class="particle particle-1"></div>
      <div class="particle particle-2"></div>
      <div class="particle particle-3"></div>
      <div class="particle particle-4"></div>
      <div class="particle particle-5"></div>
    </div>

    <!-- NEW: Top navigation bar instead of sidebar -->
    <nav class="relative z-20 bg-slate-900/80 backdrop-blur-xl border-b border-slate-700/50 shadow-2xl">
      <div class="max-w-7xl mx-auto px-6">
        <div class="flex items-center justify-between h-20">
          <!-- Logo -->
          <div class="flex items-center space-x-3">
            <div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-cyan-500 via-blue-500 to-purple-600 flex items-center justify-center shadow-lg shadow-blue-500/50">
              <svg class="w-7 h-7 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
            </div>
            <h2 class="text-white font-bold text-2xl bg-gradient-to-r from-cyan-400 to-blue-400 bg-clip-text text-transparent">Auction Site</h2>
          </div>

          <!-- Center Navigation Links -->
          <div class="flex items-center space-x-2">
            <router-link to="/home" class="px-4 py-2.5 bg-gradient-to-r from-cyan-600/30 to-blue-600/30 text-white rounded-xl border border-cyan-500/40 font-medium">
              Home
            </router-link>
            <router-link to="/browse" class="px-4 py-2.5 text-slate-300 hover:bg-slate-800/50 hover:text-white rounded-xl transition-all">
              Browse
            </router-link>
            <router-link to="/my-bids" class="px-4 py-2.5 text-slate-300 hover:bg-slate-800/50 hover:text-white rounded-xl transition-all">
              My Bids
            </router-link>
            <router-link to="/my-auctions" class="px-4 py-2.5 text-slate-300 hover:bg-slate-800/50 hover:text-white rounded-xl transition-all">
              My Auctions
            </router-link>
            <router-link to="/messages" class="px-4 py-2.5 text-slate-300 hover:bg-slate-800/50 hover:text-white rounded-xl transition-all">
              Messages
            </router-link>
          </div>

          <!-- Right Actions -->
          <div class="flex items-center space-x-3">
            <!-- Added profile link -->
            <router-link to="/profile" class="flex items-center space-x-2 p-2.5 text-slate-300 hover:text-white hover:bg-slate-800/50 rounded-xl transition-all">
              <div v-if="authStore.user?.profile_image_url" class="w-8 h-8 rounded-lg overflow-hidden">
                <img :src="authStore.user.profile_image_url" alt="Profile" class="w-full h-full object-cover" />
              </div>
              <div v-else class="w-8 h-8 rounded-lg bg-gradient-to-br from-cyan-500 to-blue-600 flex items-center justify-center text-white font-bold text-sm">
                {{ authStore.user?.username.charAt(0).toUpperCase() }}
              </div>
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
              </svg>
            </router-link>
            
            <router-link to="/notifications" class="relative p-3 text-slate-300 hover:text-white hover:bg-slate-800/50 rounded-xl transition-all">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
              </svg>
              <span class="absolute top-2 right-2 w-2 h-2 bg-pink-500 rounded-full"></span>
            </router-link>
            <router-link to="/settings" class="p-3 text-slate-300 hover:text-white hover:bg-slate-800/50 rounded-xl transition-all">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
              </svg>
            </router-link>
            <button
              @click="confirmLogout"
              class="px-4 py-2.5 bg-red-500/20 hover:bg-red-500/30 text-red-400 hover:text-red-300 rounded-xl font-medium transition-all"
            >
              Logout
            </button>
          </div>
        </div>
      </div>
    </nav>

    <!-- NEW: Main content with centered hero layout -->
    <main class="relative z-10 max-w-7xl mx-auto px-6 py-12">
      <!-- Hero Welcome Section -->
      <div class="text-center mb-16">
        <h1 class="text-6xl font-bold mb-4 animated-gradient-text">Welcome Back!</h1>
        <p class="text-slate-300 text-xl">Track your auctions and manage your bids</p>
      </div>

      <!-- Updated stats cards to use real data from API -->
      <div class="flex space-x-6 mb-12">
        <div class="flex-1 bg-gradient-to-br from-cyan-600/20 to-blue-600/20 backdrop-blur-xl border border-cyan-500/30 rounded-3xl p-8 shadow-2xl hover:scale-105 transition-transform">
          <div class="flex items-center justify-between">
            <div>
              <div v-if="loadingStats" class="h-12 w-16 bg-slate-700/50 rounded animate-pulse mb-2"></div>
              <div v-else class="text-5xl font-bold text-white mb-2 counter-animation">{{ stats.activeAuctions }}</div>
              <div class="text-cyan-300 font-semibold text-lg">Active Auctions</div>
              <div class="text-slate-400 text-sm mt-1">Auctions you're bidding on</div>
            </div>
            <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-cyan-500 to-blue-600 flex items-center justify-center floating-icon">
              <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" />
              </svg>
            </div>
          </div>
        </div>

        <div class="flex-1 bg-gradient-to-br from-purple-600/20 to-pink-600/20 backdrop-blur-xl border border-purple-500/30 rounded-3xl p-8 shadow-2xl hover:scale-105 transition-transform">
          <div class="flex items-center justify-between">
            <div>
              <div v-if="loadingStats" class="h-12 w-16 bg-slate-700/50 rounded animate-pulse mb-2"></div>
              <div v-else class="text-5xl font-bold text-white mb-2 counter-animation">{{ stats.totalBids }}</div>
              <div class="text-purple-300 font-semibold text-lg">Total Bids</div>
              <div class="text-slate-400 text-sm mt-1">Bids you've placed</div>
            </div>
            <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-purple-500 to-pink-600 flex items-center justify-center floating-icon" style="animation-delay: 0.3s">
              <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
          </div>
        </div>

        <div class="flex-1 bg-gradient-to-br from-emerald-600/20 to-green-600/20 backdrop-blur-xl border border-emerald-500/30 rounded-3xl p-8 shadow-2xl hover:scale-105 transition-transform">
          <div class="flex items-center justify-between">
            <div>
              <div v-if="loadingStats" class="h-12 w-16 bg-slate-700/50 rounded animate-pulse mb-2"></div>
              <div v-else class="text-5xl font-bold text-white mb-2 counter-animation">${{ stats.totalSpent }}</div>
              <div class="text-emerald-300 font-semibold text-lg">Total Spent</div>
              <div class="text-slate-400 text-sm mt-1">On won auctions</div>
            </div>
            <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-emerald-500 to-green-600 flex items-center justify-center floating-icon" style="animation-delay: 0.6s">
              <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138z" />
              </svg>
            </div>
          </div>
        </div>
      </div>

      <!-- Single column layout with stacked sections -->
      <div class="space-y-8">
        <!-- Updated Active Bids Section to fetch and display real data with empty state -->
        <div class="bg-slate-900/50 backdrop-blur-xl border border-slate-700/50 rounded-3xl p-8 shadow-2xl">
          <div class="flex items-center justify-between mb-6">
            <h2 class="text-3xl font-bold text-white flex items-center">
              <div class="w-14 h-14 rounded-2xl bg-gradient-to-br from-cyan-500 to-blue-600 flex items-center justify-center mr-4 shadow-lg floating-icon">
                <svg class="w-7 h-7 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" />
                </svg>
              </div>
              Your Active Bids
            </h2>
            <span v-if="activeBids.length > 0" class="px-4 py-2 bg-cyan-500/20 text-cyan-300 text-lg font-bold rounded-full">{{ activeBids.length }} Active</span>
          </div>
          
          <!-- Empty state -->
          <div v-if="loadingBids" class="text-center py-8">
            <div class="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-cyan-500"></div>
            <p class="text-slate-400 mt-2">Loading bids...</p>
          </div>
          
          <div v-else-if="activeBids.length === 0" class="text-center py-12">
            <svg class="w-16 h-16 text-slate-600 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <h3 class="text-xl font-bold text-white mb-2">No Active Bids</h3>
            <p class="text-slate-400 mb-4">Start bidding on items you're interested in</p>
            <router-link to="/browse" class="inline-flex items-center px-6 py-3 bg-gradient-to-r from-cyan-600 to-blue-600 hover:from-cyan-700 hover:to-blue-700 text-white rounded-xl font-semibold transition-all shadow-lg">
              Browse Auctions
            </router-link>
          </div>
          
          <div v-else>
            <div class="grid grid-cols-2 gap-4">
              <div v-for="bid in activeBids.slice(0, 4)" :key="bid.id" class="flex items-center justify-between p-6 bg-gradient-to-br from-slate-800/70 to-slate-800/50 rounded-2xl border transition-all" :class="bid.is_winning ? 'border-cyan-500/20 hover:border-cyan-500/40' : 'border-red-500/20 hover:border-red-500/40'">
                <div>
                  <p class="text-white font-semibold text-lg mb-1">{{ bid.item.title }}</p>
                  <p class="text-slate-400">{{ bid.is_winning ? `Your bid: $${bid.amount}` : `Current: $${bid.item.current_price}` }}</p>
                </div>
                <span :class="bid.is_winning ? 'bg-emerald-500/20 text-emerald-300' : 'bg-red-500/20 text-red-300'" class="px-4 py-2 text-sm font-bold rounded-full">
                  {{ bid.is_winning ? 'Winning' : 'Outbid' }}
                </span>
              </div>
            </div>
            <router-link to="/my-bids" class="mt-6 block text-center text-cyan-400 hover:text-cyan-300 font-bold text-lg">
              View All Bids →
            </router-link>
          </div>
        </div>

        <!-- Quick Actions Grid -->
        <div class="grid grid-cols-4 gap-6">
          <router-link to="/create" class="bg-gradient-to-br from-blue-600/30 to-purple-600/30 backdrop-blur-xl border border-blue-500/30 rounded-3xl p-8 hover:scale-105 transition-transform text-center shadow-xl">
            <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center mx-auto mb-4 floating-icon">
              <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
              </svg>
            </div>
            <p class="text-white font-bold text-lg">Create Auction</p>
            <p class="text-slate-400 text-sm mt-1">List a new item</p>
          </router-link>

          <router-link to="/browse" class="bg-gradient-to-br from-purple-600/30 to-pink-600/30 backdrop-blur-xl border border-purple-500/30 rounded-3xl p-8 hover:scale-105 transition-transform text-center shadow-xl">
            <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-purple-500 to-pink-600 flex items-center justify-center mx-auto mb-4 floating-icon" style="animation-delay: 0.2s">
              <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
            </div>
            <p class="text-white font-bold text-lg">Browse Items</p>
            <p class="text-slate-400 text-sm mt-1">Find auctions</p>
          </router-link>

          <router-link to="/messages" class="bg-gradient-to-br from-pink-600/30 to-rose-600/30 backdrop-blur-xl border border-pink-500/30 rounded-3xl p-8 hover:scale-105 transition-transform text-center shadow-xl">
            <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-pink-500 to-rose-600 flex items-center justify-center mx-auto mb-4 floating-icon" style="animation-delay: 0.4s">
              <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
              </svg>
            </div>
            <p class="text-white font-bold text-lg">Messages</p>
            <p class="text-slate-400 text-sm mt-1">View messages</p>
          </router-link>

          <router-link to="/my-auctions" class="bg-gradient-to-br from-emerald-600/30 to-green-600/30 backdrop-blur-xl border border-emerald-500/30 rounded-3xl p-8 hover:scale-105 transition-transform text-center shadow-xl">
            <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-emerald-500 to-green-600 flex items-center justify-center mx-auto mb-4 floating-icon" style="animation-delay: 0.6s">
              <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138z" />
              </svg>
            </div>
            <p class="text-white font-bold text-lg">My Auctions</p>
            <p class="text-slate-400 text-sm mt-1">Manage listings</p>
          </router-link>
        </div>

        <!-- Updated Recent Activity to fetch and display real data with empty state -->
        <div class="bg-slate-900/50 backdrop-blur-xl border border-slate-700/50 rounded-3xl p-8 shadow-2xl">
          <h2 class="text-3xl font-bold text-white mb-6 flex items-center">
            <div class="w-14 h-14 rounded-2xl bg-gradient-to-br from-orange-500 to-amber-600 flex items-center justify-center mr-4 shadow-lg floating-icon" style="animation-delay: 0.8s">
              <svg class="w-7 h-7 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
            Recent Activity
          </h2>
          
          <!-- Empty state -->
          <div v-if="loadingActivity" class="text-center py-8">
            <div class="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-orange-500"></div>
            <p class="text-slate-400 mt-2">Loading activity...</p>
          </div>
          
          <div v-else-if="recentActivity.length === 0" class="text-center py-12">
            <svg class="w-16 h-16 text-slate-600 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <h3 class="text-xl font-bold text-white mb-2">No Recent Activity</h3>
            <p class="text-slate-400">Your activity will appear here</p>
          </div>
          
          <div v-else class="grid grid-cols-3 gap-6">
            <div v-for="activity in recentActivity.slice(0, 3)" :key="activity.id" class="p-6 bg-gradient-to-br rounded-2xl border" :class="activity.type === 'bid' ? 'from-cyan-600/20 to-blue-600/20 border-cyan-500/30' : activity.type === 'won' ? 'from-emerald-600/20 to-green-600/20 border-emerald-500/30' : 'from-purple-600/20 to-pink-600/20 border-purple-500/30'">
              <div class="flex items-center space-x-4 mb-3">
                <div class="w-12 h-12 rounded-xl bg-gradient-to-br flex items-center justify-center" :class="activity.type === 'bid' ? 'from-cyan-500 to-blue-600' : activity.type === 'won' ? 'from-emerald-500 to-green-600' : 'from-purple-500 to-pink-600'">
                  <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path v-if="activity.type === 'bid'" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                    <path v-else-if="activity.type === 'won'" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138z" />
                    <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
                  </svg>
                </div>
                <div class="flex-1">
                  <p class="text-white font-semibold">{{ activity.title }}</p>
                  <p :class="activity.type === 'bid' ? 'text-cyan-300' : activity.type === 'won' ? 'text-emerald-300' : 'text-purple-300'" class="text-sm">{{ activity.time }}</p>
                </div>
              </div>
              <p class="text-slate-300">{{ activity.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed, onMounted, onActivated, reactive } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '../stores/auth';
import { useItemsStore } from '../stores/items';

interface BidWithItem {
  id: number;
  amount: string;
  is_winning: boolean;
  created_at: string;
  item: {
    id: number;
    title: string;
    current_price: string;
    is_active: boolean;
  };
}

interface Activity {
  id: string;
  type: 'bid' | 'won' | 'listed';
  title: string;
  time: string;
  description: string;
}

interface Stats {
  activeAuctions: number;
  totalBids: number;
  totalSpent: string;
}

export default defineComponent({
  name: 'HomePage',
  setup() {
    const router = useRouter();
    const authStore = useAuthStore();
    const itemsStore = useItemsStore();
    
    const searchQuery = ref('');
    const loading = computed(() => itemsStore.loading);
    const filteredItems = computed(() => itemsStore.filteredItems);
    
    const activeBids = ref<BidWithItem[]>([]);
    const loadingBids = ref(true);
    const recentActivity = ref<Activity[]>([]);
    const loadingActivity = ref(true);
    
    const stats = reactive<Stats>({
      activeAuctions: 0,
      totalBids: 0,
      totalSpent: '0.00',
    });
    const loadingStats = ref(true);

    const fetchStats = async () => {
      loadingStats.value = true;
      try {
        const response = await fetch('/api/stats/', {
          credentials: 'include',
        });
        const data = await response.json();
        if (data.ok) {
          stats.activeAuctions = data.stats.active_auctions;
          stats.totalBids = data.stats.total_bids;
          stats.totalSpent = data.stats.total_spent;
        }
      } catch (err) {
        console.error('Failed to fetch stats:', err);
      } finally {
        loadingStats.value = false;
      }
    };

    const fetchActiveBids = async () => {
      loadingBids.value = true;
      try {
        const response = await fetch('/api/bids/', {
          credentials: 'include',
        });
        const data = await response.json();
        if (data.ok) {
          activeBids.value = data.bids.filter((bid: BidWithItem) => bid.item.is_active);
        }
      } catch (err) {
        console.error('Failed to fetch bids:', err);
      } finally {
        loadingBids.value = false;
      }
    };

    const fetchRecentActivity = async () => {
      loadingActivity.value = true;
      try {
        const [bidsResponse, itemsResponse] = await Promise.all([
          fetch('/api/bids/', { credentials: 'include' }),
          fetch('/api/items/?my_items=true', { credentials: 'include' })
        ]);
        
        const bidsData = await bidsResponse.json();
        const itemsData = await itemsResponse.json();
        
        const activities: Activity[] = [];
        
        // Add recent bids
        if (bidsData.ok && bidsData.bids) {
          bidsData.bids.slice(0, 5).forEach((bid: BidWithItem) => {
            activities.push({
              id: `bid-${bid.id}`,
              type: bid.is_winning && !bid.item.is_active ? 'won' : 'bid',
              title: bid.is_winning && !bid.item.is_active ? 'Auction Won' : 'Bid Placed',
              time: formatActivityTime(bid.created_at),
              description: `${bid.item.title} - $${bid.amount}`
            });
          });
        }
        
        // Add recent listings
        if (itemsData.ok && itemsData.items) {
          itemsData.items.slice(0, 3).forEach((item: any) => {
            activities.push({
              id: `item-${item.id}`,
              type: 'listed',
              title: 'New Auction',
              time: formatActivityTime(item.created_at || item.ends_at),
              description: `${item.title} Listed`
            });
          });
        }
        
        // Sort by most recent
        recentActivity.value = activities.slice(0, 6);
      } catch (err) {
        console.error('Failed to fetch activity:', err);
      } finally {
        loadingActivity.value = false;
      }
    };

    const formatActivityTime = (dateString: string): string => {
      const date = new Date(dateString);
      const now = new Date();
      const diff = now.getTime() - date.getTime();
      const minutes = Math.floor(diff / 60000);
      const hours = Math.floor(diff / 3600000);
      const days = Math.floor(diff / 86400000);
      
      if (minutes < 1) return 'Just now';
      if (minutes < 60) return `${minutes}m ago`;
      if (hours < 24) return `${hours}h ago`;
      if (days === 1) return 'Yesterday';
      return `${days}d ago`;
    };

    const refreshAllData = () => {
      itemsStore.fetchItems();
      fetchStats();
      fetchActiveBids();
      fetchRecentActivity();
    };

    const handleSearch = () => {
      // Placeholder for handleSearch function
    };

    const goToItem = (itemId: number) => {
      // Placeholder for goToItem function
      router.push(`/item/${itemId}`);
    };

    const confirmLogout = () => {
      // Placeholder for confirmLogout function
      if (window.confirm('Are you sure you want to log out?')) {
        authStore.logout();
        router.push('/login');
      }
    };

    const formatDate = (dateString: string): string => {
      // Placeholder for formatDate function
      return new Date(dateString).toLocaleDateString();
    };

    onMounted(() => {
      refreshAllData();
    });

    onActivated(() => {
      refreshAllData();
    });


    return {
      authStore,
      searchQuery,
      loading,
      filteredItems,
      activeBids,
      loadingBids,
      recentActivity,
      loadingActivity,
      stats,
      loadingStats,
      handleSearch,
      goToItem,
      confirmLogout,
      formatDate,
    };
  },
});
</script>

<style scoped>
/* Kept existing animations but added new ones for the redesigned layout */
/* Animated gradient orbs */
.animated-orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(100px);
  opacity: 0.3;
  animation: orbFloat 25s infinite ease-in-out;
}

.orb-1 {
  width: 500px;
  height: 500px;
  background: linear-gradient(135deg, #3b82f6, #8b5cf6);
  top: -10%;
  left: -10%;
}

.orb-2 {
  width: 400px;
  height: 400px;
  background: linear-gradient(135deg, #a855f7, #ec4899);
  bottom: -10%;
  right: -10%;
  animation-delay: 10s;
}

.orb-3 {
  width: 450px;
  height: 450px;
  background: linear-gradient(135deg, #06b6d4, #3b82f6);
  top: 40%;
  right: 20%;
  animation-delay: 5s;
}

@keyframes orbFloat {
  0%, 100% {
    transform: translate(0, 0) scale(1);
  }
  33% {
    transform: translate(100px, -80px) scale(1.1);
  }
  66% {
    transform: translate(-80px, 100px) scale(0.9);
  }
}

/* Floating particles */
.particle {
  position: absolute;
  background: radial-gradient(circle, rgba(147, 51, 234, 0.6) 0%, rgba(59, 130, 246, 0.3) 50%, transparent 70%);
  border-radius: 50%;
  animation: particleFloat 20s infinite ease-in-out;
}

.particle-1 {
  width: 4px;
  height: 4px;
  top: 10%;
  left: 15%;
  animation-duration: 18s;
}

.particle-2 {
  width: 6px;
  height: 6px;
  top: 70%;
  left: 25%;
  animation-duration: 22s;
  animation-delay: 2s;
}

.particle-3 {
  width: 3px;
  height: 3px;
  top: 40%;
  right: 20%;
  animation-duration: 25s;
  animation-delay: 4s;
}

.particle-4 {
  width: 5px;
  height: 5px;
  top: 80%;
  right: 35%;
  animation-duration: 20s;
  animation-delay: 1s;
}

.particle-5 {
  width: 4px;
  height: 4px;
  top: 25%;
  left: 60%;
  animation-duration: 24s;
  animation-delay: 3s;
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

/* Animated gradient text */
.animated-gradient-text {
  background: linear-gradient(90deg, #06b6d4, #3b82f6, #a855f7, #ec4899);
  background-size: 300% 300%;
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gradientShift 6s ease infinite;
}

@keyframes gradientShift {
  0%, 100% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
}

/* Counter animation */
.counter-animation {
  animation: countUp 2s ease-out;
}

@keyframes countUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Floating icon animation */
.floating-icon {
  animation: iconFloat 3s ease-in-out infinite;
}

@keyframes iconFloat {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-10px);
  }
}
</style>
