<template>
  <div class="min-h-screen bg-gradient-to-br from-slate-950 via-indigo-950 to-purple-950 relative overflow-hidden">
    <!-- Particles like messages page -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
      <div class="particle particle-1"></div>
      <div class="particle particle-2"></div>
      <div class="particle particle-3"></div>
    </div>

    <!-- Header / Navigation -->
    <nav class="bg-slate-900/50 backdrop-blur-md border-b border-slate-700/50 sticky top-0 z-50 shadow-sm">
      <div class="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
        <div class="flex items-center gap-6">
          <router-link to="/home" class="flex items-center gap-3 text-sm font-medium text-purple-400 hover:text-purple-300 transition-colors">
            ← Back to Dashboard
          </router-link>
          <h1 class="text-2xl font-bold text-white">Create Auction</h1>
        </div>
      </div>
    </nav>

    <main class="max-w-6xl mx-auto px-6 py-12">
      <!-- Page title -->
      <div class="text-center mb-12">
        <h1 class="text-5xl font-bold text-white mb-4">List Your Item</h1>
        <p class="text-xl text-slate-400">Create an auction and start selling</p>
      </div>

      <!-- Form card -->
      <div class="bg-slate-900 rounded-2xl shadow-lg border border-slate-800 p-10">
        <form @submit.prevent="createItem" class="space-y-6">
          <div>
            <label for="title" class="block text-sm font-bold text-slate-300 mb-2">
              Item Title *
            </label>
            <input
              id="title"
              v-model="formData.title"
              type="text"
              required
              placeholder="e.g., Vintage Leather Jacket - Like New"
              class="w-full px-4 py-4 bg-slate-800 border border-slate-700 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-blue-500 placeholder-slate-500 transition-all"
            />
          </div>

          <div>
            <label for="description" class="block text-sm font-bold text-slate-300 mb-2">
              Description *
            </label>
            <textarea
              id="description"
              v-model="formData.description"
              rows="6"
              required
              placeholder="Provide detailed information about your item including condition, size, features, etc."
              class="w-full px-4 py-4 bg-slate-800 border border-slate-700 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none placeholder-slate-500 transition-all"
            ></textarea>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label for="starting_price" class="block text-sm font-bold text-slate-300 mb-2">
                Starting Price ($) *
              </label>
              <div class="relative">
                <span class="absolute left-4 top-1/2 transform -translate-y-1/2 text-slate-400 font-bold text-lg">$</span>
                <input
                  id="starting_price"
                  v-model.number="formData.starting_price"
                  type="number"
                  min="0.01"
                  step="0.01"
                  required
                  placeholder="0.00"
                  class="w-full pl-8 pr-4 py-4 bg-slate-800 border border-slate-700 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all"
                />
              </div>
            </div>

            <div>
              <label for="ends_at" class="block text-sm font-bold text-slate-300 mb-2">
                Auction End Date & Time *
              </label>
              <input
                id="ends_at"
                v-model="formData.ends_at"
                type="datetime-local"
                required
                :min="minDateTime"
                class="w-full px-4 py-4 bg-slate-800 border border-slate-700 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all"
              />
            </div>
          </div>

          <div>
            <label for="image" class="block text-sm font-bold text-slate-300 mb-2">
              Item Image
            </label>
            <div class="border-2 border-dashed border-slate-700 rounded-xl p-8 text-center hover:border-blue-500 transition-colors bg-slate-800/30">
              <input
                id="image"
                type="file"
                accept="image/*"
                @change="handleImageUpload"
                class="hidden"
              />
              <label for="image" class="cursor-pointer">
                <svg class="w-16 h-16 text-slate-500 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
                </svg>
                <p class="text-slate-300 font-medium mb-1">
                  {{ formData.image ? formData.image.name : 'Click to upload an image' }}
                </p>
                <p class="text-slate-500 text-sm">PNG, JPG up to 10MB</p>
              </label>
            </div>
          </div>

          <div v-if="error" class="p-4 bg-red-500/10 border border-red-500/50 rounded-lg">
            <p class="text-red-400 font-medium">{{ error }}</p>
          </div>

          <div v-if="success" class="p-4 bg-green-500/10 border border-green-500/50 rounded-lg">
            <p class="text-green-400 font-medium">{{ success }}</p>
          </div>

          <button
            type="submit"
            :disabled="creating"
            class="w-full bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white font-bold py-5 px-6 rounded-xl transition-all duration-300 shadow-lg disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {{ creating ? 'Creating Listing...' : 'Create Auction Listing' }}
          </button>
        </form>
      </div>
    </main>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { fetchWithCsrf } from '../utils/csrf';

export default defineComponent({
  name: 'CreateItemPage',
  setup() {
    const router = useRouter();

    const formData = ref({
      title: '',
      description: '',
      starting_price: 0,
      ends_at: '',
      image: null as File | null,
    });

    const creating = ref(false);
    const error = ref('');
    const success = ref('');

    const minDateTime = computed(() => {
      const now = new Date();
      now.setHours(now.getHours() + 1);
      return now.toISOString().slice(0, 16);
    });

    onMounted(async () => {
      try {
        await fetch('/api/csrf/', {
          credentials: 'include',
        });
      } catch (err) {
        console.error('Failed to fetch CSRF token:', err);
      }
    });

    const handleImageUpload = (event: Event) => {
      const target = event.target as HTMLInputElement;
      if (target.files && target.files[0]) {
        formData.value.image = target.files[0];
      }
    };

    const createItem = async () => {
      creating.value = true;
      error.value = '';
      success.value = '';

      try {
        const payload = new FormData();
        payload.append('title', formData.value.title);
        payload.append('description', formData.value.description);
        payload.append('starting_price', formData.value.starting_price.toString());
        
        const endsAt = formData.value.ends_at.replace('T', ' ');
        payload.append('ends_at', endsAt);
        
        if (formData.value.image) {
          payload.append('image', formData.value.image);
        }

        const response = await fetchWithCsrf('/api/items/', {
          method: 'POST',
          body: payload,
        });

        const data = await response.json();

        if (data.ok) {
          success.value = 'Item created successfully! Redirecting...';
          setTimeout(() => {
            router.push({ name: 'BrowseAuctions' });
          }, 1500);
        } else {
          error.value = data.error || 'Failed to create item';
        }
      } catch (err) {
        error.value = 'An error occurred. Please try again.';
        console.error('Error creating item:', err);
      } finally {
        creating.value = false;
      }
    };

    return { formData, creating, error, success, minDateTime, handleImageUpload, createItem };
  },
});
</script>

<style scoped>
.particle {
  position: absolute;
  background: radial-gradient(circle, rgba(147,51,234,0.6) 0%, rgba(59,130,246,0.3) 50%, transparent 70%);
  border-radius: 50%;
  animation: particleFloat 20s infinite ease-in-out;
}
.particle-1 { width:4px; height:4px; top:15%; left:20%; animation-duration:18s; }
.particle-2 { width:6px; height:6px; top:70%; right:25%; animation-duration:22s; animation-delay:2s; }
.particle-3 { width:5px; height:5px; top:40%; right:15%; animation-duration:20s; animation-delay:4s; }

@keyframes particleFloat {
  0%,100% { transform: translate(0,0) scale(1); opacity:0; }
  10% { opacity:1; }
  50% { transform: translate(100px,-100px) scale(1.5); opacity:0.8; }
  90% { opacity:1; }
}
</style>
