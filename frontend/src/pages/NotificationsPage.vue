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
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
                </svg>
              </div>
              <div>
                <h1 class="text-xl font-bold text-white">Notifications</h1>
                <p class="text-xs text-slate-400">Stay updated</p>
              </div>
            </router-link>
          </div>
          
          <router-link to="/home" class="text-sm font-medium text-purple-400 hover:text-purple-300 transition-colors">
            ← Back to Dashboard
          </router-link>
        </div>
      </div>
    </nav>
    
    <div class="max-w-4xl mx-auto px-6 py-8">
      <!-- Added loading state and dynamic notifications -->
      <div v-if="loading" class="text-center py-12">
        <div class="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-purple-500"></div>
        <p class="text-slate-400 mt-4">Loading notifications...</p>
      </div>

      <div v-else>
        <div class="mb-6 flex items-center justify-between">
          <h2 class="text-2xl font-bold text-white">
            All Notifications
            <span v-if="unreadCount > 0" class="ml-2 text-sm font-medium text-blue-400">({{ unreadCount }} unread)</span>
          </h2>
          <button 
            v-if="unreadCount > 0"
            @click="markAllRead"
            class="text-sm font-medium text-blue-400 hover:text-blue-300 transition-colors"
          >
            Mark all as read
          </button>
        </div>
        
        <div v-if="notifications.length > 0" class="space-y-4">
          <div 
            v-for="notification in notifications" 
            :key="notification.id"
            @click="handleNotificationClick(notification)"
            class="bg-slate-900 rounded-2xl p-6 shadow-lg cursor-pointer transition-all hover:bg-slate-800/90"
            :class="{
              'border border-blue-900/50': !notification.is_read,
              'border border-slate-800': notification.is_read,
              'opacity-70': notification.is_read
            }"
          >
            <div class="flex items-start gap-4">
              <div 
                class="w-12 h-12 rounded-xl flex items-center justify-center flex-shrink-0"
                :class="getNotificationIconClass(notification.type)"
              >
                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path 
                    stroke-linecap="round" 
                    stroke-linejoin="round" 
                    stroke-width="2" 
                    :d="getNotificationIconPath(notification.type)"
                  />
                </svg>
              </div>
              <div class="flex-1">
                <h4 class="font-semibold text-white">{{ notification.title }}</h4>
                <p class="text-sm text-slate-400 mt-1">{{ notification.message }}</p>
                <p class="text-xs text-slate-500 mt-2">{{ formatTime(notification.created_at) }}</p>
              </div>
              <span 
                v-if="!notification.is_read"
                class="w-2 h-2 bg-blue-500 rounded-full flex-shrink-0"
              ></span>
            </div>
          </div>
        </div>

        <!-- Empty state -->
        <div v-else class="text-center py-16">
          <div class="w-20 h-20 bg-slate-800/50 rounded-full flex items-center justify-center mx-auto mb-4">
            <svg class="w-10 h-10 text-slate-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
            </svg>
          </div>
          <h3 class="text-xl font-semibold text-white mb-2">No notifications yet</h3>
          <p class="text-slate-400">You'll see notifications here when there's activity</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { fetchWithCsrf } from '../utils/csrf';
import type { Notification } from '../types';

export default defineComponent({
  name: 'NotificationsPage',
  setup() {
    const router = useRouter();
    const notifications = ref<Notification[]>([]);
    const unreadCount = ref(0);
    const loading = ref(true);

    const fetchNotifications = async () => {
      loading.value = true;
      try {
        const response = await fetch('/api/notifications/', {
          credentials: 'include',
        });

        if (response.ok) {
          const data = await response.json();
          notifications.value = data.notifications || [];
          unreadCount.value = data.unread_count || 0;
        }
      } catch (error) {
        console.error('Failed to fetch notifications:', error);
      } finally {
        loading.value = false;
      }
    };

    const markAllRead = async () => {
      try {
        await fetchWithCsrf('/api/notifications/mark-all-read/', {
          method: 'POST',
        });
        
        notifications.value = notifications.value.map(n => ({ ...n, is_read: true }));
        unreadCount.value = 0;
      } catch (error) {
        console.error('Failed to mark all as read:', error);
      }
    };

    const handleNotificationClick = async (notification: Notification) => {
      if (!notification.is_read) {
        try {
          await fetchWithCsrf(`/api/notifications/${notification.id}/read/`, {
            method: 'POST',
          });
          
          notification.is_read = true;
          unreadCount.value = Math.max(0, unreadCount.value - 1);
        } catch (error) {
          console.error('Failed to mark notification as read:', error);
        }
      }

      if (notification.link) {
        router.push(notification.link);
      }
    };

    const getNotificationIconClass = (type: string) => {
      const classes: Record<string, string> = {
        question: 'bg-gradient-to-br from-violet-500 to-purple-500',
        reply: 'bg-gradient-to-br from-blue-500 to-blue-600',
        bid: 'bg-gradient-to-br from-emerald-500 to-teal-500',
        outbid: 'bg-gradient-to-br from-orange-500 to-red-500',
        won: 'bg-gradient-to-br from-yellow-500 to-amber-500',
      };
      return classes[type] || 'bg-gradient-to-br from-slate-500 to-slate-600';
    };

    const getNotificationIconPath = (type: string) => {
      const paths: Record<string, string> = {
        question: 'M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z',
        reply: 'M3 10h10a8 8 0 018 8v2M3 10l6 6m-6-6l6-6',
        bid: 'M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z',
        outbid: 'M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z',
        won: 'M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z',
      };
      return paths[type] || 'M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9';
    };

    const formatTime = (dateString: string) => {
      const date = new Date(dateString);
      const now = new Date();
      const diffMs = now.getTime() - date.getTime();
      const diffMins = Math.floor(diffMs / 60000);
      const diffHours = Math.floor(diffMs / 3600000);
      const diffDays = Math.floor(diffMs / 86400000);

      if (diffMins < 1) return 'Just now';
      if (diffMins < 60) return `${diffMins} minute${diffMins > 1 ? 's' : ''} ago`;
      if (diffHours < 24) return `${diffHours} hour${diffHours > 1 ? 's' : ''} ago`;
      if (diffDays < 7) return `${diffDays} day${diffDays > 1 ? 's' : ''} ago`;
      return date.toLocaleDateString();
    };

    onMounted(() => {
      fetchNotifications();
    });

    return {
      notifications,
      unreadCount,
      loading,
      markAllRead,
      handleNotificationClick,
      getNotificationIconClass,
      getNotificationIconPath,
      formatTime,
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
