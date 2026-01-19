<template>
  <div class="min-h-screen bg-gradient-to-br from-slate-950 via-indigo-950 to-purple-950 flex items-center justify-center p-4 relative overflow-hidden">
    <!-- Enhanced background -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none z-0">
      <div class="orb orb-blue"></div>
      <div class="orb orb-purple"></div>
      <div class="orb orb-pink"></div>
      <div class="orb orb-orange"></div>
      <div class="orb orb-green"></div>
    </div>

    <!-- Added animated particles like signup page -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
      <div class="particle particle-1"></div>
      <div class="particle particle-2"></div>
      <div class="particle particle-3"></div>
      <div class="particle particle-4"></div>
      <div class="particle particle-5"></div>
      <div class="particle particle-6"></div>
    </div>

    <!-- Added floating geometric shapes like signup page -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
      <div class="floating-shape shape-1"></div>
      <div class="floating-shape shape-2"></div>
      <div class="floating-shape shape-3"></div>
    </div>

    <div class="w-full max-w-md relative z-20 pointer-events-auto">
      <!-- Better header styling -->
      <div class="text-center mb-8">
        <h2 class="text-3xl font-bold text-white mb-2">Welcome Back</h2>
        <p class="text-slate-400 text-base">Sign in to your account</p>
      </div>

      <div class="bg-slate-900/50 backdrop-blur-md rounded-2xl p-8 border border-slate-800 shadow-2xl">
        <form @submit.prevent="handleLogin" class="space-y-5">
          <div>
            <label for="username" class="block text-sm font-medium text-slate-300 mb-2">
              Username <span class="text-red-500">*</span>
            </label>
            <input
              id="username"
              v-model="credentials.username"
              type="text"
              required
              autocomplete="username"
              class="w-full px-4 py-3.5 bg-slate-800/70 border border-slate-700 rounded-xl text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-purple-500 transition-all duration-200"
              placeholder="Enter your username"
            />
          </div>

          <div>
            <label for="password" class="block text-sm font-medium text-slate-300 mb-2">
              Password <span class="text-red-500">*</span>
            </label>
            <div class="relative">
              <input
                id="password"
                v-model="credentials.password"
                :type="showPassword ? 'text' : 'password'"
                required
                autocomplete="current-password"
                class="w-full px-4 py-3.5 bg-slate-800/70 border border-slate-700 rounded-xl text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-purple-500 transition-all duration-200"
                placeholder="Enter your password"
              />
              <button 
                type="button" 
                @click="showPassword = !showPassword"
                class="absolute right-4 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-300 transition-colors p-1"
              >
                <svg v-if="!showPassword" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                </svg>
                <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21" />
                </svg>
              </button>
            </div>
          </div>

          <!-- Added error message display -->
          <div v-if="error" class="p-4 bg-red-500/20 border border-red-500/50 rounded-xl">
            <div class="flex items-start space-x-3">
              <svg class="w-5 h-5 text-red-400 flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd" />
              </svg>
              <p class="text-red-300 text-sm font-medium">{{ error }}</p>
            </div>
          </div>

          <button
            type="submit"
            :disabled="loading"
            class="w-full bg-gradient-to-r from-blue-600 via-purple-600 to-pink-600 hover:from-blue-500 hover:via-purple-500 hover:to-pink-500 text-white font-semibold py-3.5 px-6 rounded-xl transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed shadow-lg shadow-purple-600/30 hover:shadow-xl hover:shadow-purple-600/40 hover:scale-[1.02] active:scale-[0.98]"
          >
            <span v-if="loading" class="flex items-center justify-center space-x-2">
              <svg class="animate-spin h-5 w-5" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              <span>Signing in...</span>
            </span>
            <span v-else>Sign In</span>
          </button>
        </form>

        <div class="mt-6 text-center">
          <p class="text-slate-400 text-sm">
            Don't have an account?
            <router-link to="/signup" class="text-purple-400 hover:text-purple-300 font-medium transition-colors hover:underline ml-1">
              Sign up
            </router-link>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '../stores/auth';

export default defineComponent({
  name: 'LoginPage',
  setup() {
    const router = useRouter();
    const authStore = useAuthStore();
    
    const credentials = ref({
      username: '',
      password: '',
    });
    
    const loading = ref(false);
    const showPassword = ref(false);
    const error = ref('');

    const handleLogin = async () => {
      loading.value = true;
      error.value = '';
      
      try {
        const response = await fetch('/api/auth/login/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          credentials: 'include',
          body: JSON.stringify({
            username: credentials.value.username,
            password: credentials.value.password,
          }),
        });

        const data = await response.json();

        if (data.ok) {
          authStore.setUser(data.user);
          await router.push('/home');
        } else {
          error.value = data.error || 'Login failed';
        }
      } catch (err) {
        error.value = 'An error occurred. Please try again.';
        console.error(err);
      } finally {
        loading.value = false;
      }
    };

    return {
      credentials,
      loading,
      showPassword,
      error,
      handleLogin,
    };
  },
});
</script>

<style scoped>
/* Improved animations */
.orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
  opacity: 0.25;
  animation: float 20s infinite ease-in-out;
  pointer-events: none;
  z-index: 0;
}

.orb-blue {
  width: 400px;
  height: 400px;
  background: #3b82f6;
  top: -10%;
  left: -10%;
  animation-delay: 0s;
}

.orb-purple {
  width: 350px;
  height: 350px;
  background: #a855f7;
  top: 20%;
  right: -10%;
  animation-delay: 4s;
}

.orb-pink {
  width: 300px;
  height: 300px;
  background: #ec4899;
  bottom: -10%;
  right: 10%;
  animation-delay: 8s;
}

.orb-orange {
  width: 280px;
  height: 280px;
  background: #f97316;
  bottom: 20%;
  left: -5%;
  animation-delay: 12s;
}

.orb-green {
  width: 320px;
  height: 320px;
  background: #10b981;
  top: 50%;
  left: 50%;
  animation-delay: 16s;
}

@keyframes float {
  0%, 100% {
    transform: translate(0, 0) scale(1);
    opacity: 0.3;
  }
  33% {
    transform: translate(40px, -60px) scale(1.15);
    opacity: 0.4;
  }
  66% {
    transform: translate(-30px, 40px) scale(0.95);
    opacity: 0.35;
  }
}

/* Added particle animations matching signup page */
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

.particle-6 {
  width: 5px;
  height: 5px;
  top: 85%;
  left: 40%;
  animation-duration: 23s;
  animation-delay: 4.5s;
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

/* Added floating shape animations matching signup page */
.floating-shape {
  position: absolute;
  border: 2px solid rgba(147, 51, 234, 0.3);
  animation: shapeFloat 15s infinite ease-in-out;
}

.shape-1 {
  width: 100px;
  height: 100px;
  top: 15%;
  left: 10%;
  border-radius: 30% 70% 70% 30% / 30% 30% 70% 70%;
  background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(147, 51, 234, 0.1) 100%);
  animation-duration: 18s;
}

.shape-2 {
  width: 80px;
  height: 80px;
  top: 60%;
  right: 15%;
  border-radius: 63% 37% 54% 46% / 55% 48% 52% 45%;
  background: linear-gradient(135deg, rgba(236, 72, 153, 0.1) 0%, rgba(147, 51, 234, 0.1) 100%);
  animation-duration: 20s;
  animation-delay: 2s;
}

.shape-3 {
  width: 90px;
  height: 90px;
  bottom: 20%;
  left: 20%;
  border-radius: 50% 50% 20% 20%;
  background: linear-gradient(135deg, rgba(147, 51, 234, 0.1) 0%, rgba(59, 130, 246, 0.1) 100%);
  animation-duration: 22s;
  animation-delay: 4s;
}

@keyframes shapeFloat {
  0%, 100% {
    transform: translate(0, 0) rotate(0deg);
  }
  25% {
    transform: translate(30px, -30px) rotate(90deg);
  }
  50% {
    transform: translate(-20px, 40px) rotate(180deg);
  }
  75% {
    transform: translate(40px, 20px) rotate(270deg);
  }
}
</style>
