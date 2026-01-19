<template>
  <div class="min-h-screen bg-gradient-to-br from-slate-950 via-indigo-950 to-purple-950 flex items-center justify-center p-4 relative overflow-hidden">
    <!-- Added animated particles like signup page -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
      <div class="particle particle-1"></div>
      <div class="particle particle-2"></div>
      <div class="particle particle-3"></div>
      <div class="particle particle-4"></div>
      <div class="particle particle-5"></div>
    </div>

    <!-- Added floating geometric shapes like signup page -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
      <div class="floating-shape shape-1"></div>
      <div class="floating-shape shape-2"></div>
    </div>

    <div class="w-full max-w-md relative z-20">
      <div class="bg-slate-900/50 backdrop-blur-xl rounded-3xl p-8 md:p-12 shadow-2xl border border-slate-800">
        <div class="text-center mb-8">
          <!-- Updated icon gradient to match signup page -->
          <div class="inline-flex items-center justify-center w-16 h-16 bg-gradient-to-br from-blue-600 via-purple-600 to-pink-600 rounded-2xl mb-4 shadow-lg">
            <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 7a2 2 0 012 2m4 0a6 6 0 01-7.743 5.743L11 17H9v2H7v2H4a1 1 0 01-1-1v-2.586a1 1 0 01.293-.707l5.964-5.964A6 6 0 1121 9z" />
            </svg>
          </div>
          <h2 class="text-3xl font-bold text-white mb-2">Forgot Password?</h2>
          <p class="text-slate-400">No worries, we'll send you reset instructions</p>
        </div>
        
        <form @submit.prevent="handleSubmit" class="space-y-6">
          <div>
            <label for="email" class="block text-sm font-semibold text-slate-300 mb-2">
              Email Address
            </label>
            <input
              id="email"
              v-model="email"
              type="email"
              required
              class="w-full px-4 py-3.5 bg-slate-800/70 border border-slate-700 rounded-xl text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent transition-all"
              placeholder="you@example.com"
            />
          </div>
          
          <!-- Updated button gradient to match signup page -->
          <button
            type="submit"
            :disabled="loading"
            class="w-full bg-gradient-to-r from-blue-600 via-purple-600 to-pink-600 hover:from-blue-500 hover:via-purple-500 hover:to-pink-500 text-white font-semibold py-3.5 px-6 rounded-xl transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed shadow-lg shadow-purple-500/50 hover:shadow-xl hover:scale-[1.02] active:scale-[0.98]"
          >
            <span v-if="loading">Sending...</span>
            <span v-else>Send Reset Link</span>
          </button>
        </form>
        
        <div class="mt-8 text-center">
          <!-- Updated link color to match signup page purple theme -->
          <router-link to="/login" class="text-sm font-medium text-purple-400 hover:text-purple-300 transition-colors">
            ← Back to Sign In
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { useRouter } from 'vue-router';

export default defineComponent({
  name: 'ForgotPasswordPage',
  setup() {
    const router = useRouter();
    const email = ref('');
    const loading = ref(false);

    const handleSubmit = async () => {
      loading.value = true;
      await new Promise(resolve => setTimeout(resolve, 1000));
      loading.value = false;
      alert('Password reset link sent to your email!');
      await router.push('/login');
    };

    return {
      email,
      loading,
      handleSubmit,
    };
  },
});
</script>

<style scoped>
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
