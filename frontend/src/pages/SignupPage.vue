<template>
  <div class="min-h-screen bg-gradient-to-br from-slate-950 via-indigo-950 to-purple-950 flex items-center justify-center p-4 relative overflow-hidden">
    <!-- Animated background particles -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
      <div class="particle particle-1"></div>
      <div class="particle particle-2"></div>
      <div class="particle particle-3"></div>
      <div class="particle particle-4"></div>
      <div class="particle particle-5"></div>
      <div class="particle particle-6"></div>
      <div class="particle particle-7"></div>
      <div class="particle particle-8"></div>
    </div>

    <!-- Floating geometric shapes -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
      <div class="floating-shape shape-1"></div>
      <div class="floating-shape shape-2"></div>
      <div class="floating-shape shape-3"></div>
      <div class="floating-shape shape-4"></div>
    </div>

    <!-- Main signup card -->
    <div class="relative z-10 w-full max-w-6xl">
      <div class="grid lg:grid-cols-2 gap-8 items-center">
        <!-- Left: Branding & Features -->
        <div class="text-center lg:text-left space-y-8 px-4">
          <div class="space-y-4">
            <div class="inline-block">
              <div class="relative">
                <!-- Animated glow effect -->
                <div class="absolute -inset-2 bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500 rounded-xl opacity-75 blur-xl animate-pulse"></div>
                <h1 class="relative text-6xl font-bold bg-gradient-to-r from-blue-400 via-purple-400 to-pink-400 bg-clip-text text-transparent">
                  Auction Site
                </h1>
              </div>
            </div>
            <p class="text-xl text-slate-300">Start your bidding journey today</p>
          </div>

          <!-- Feature highlights with animated icons -->
          <div class="space-y-6">
            <div class="flex items-start space-x-4 feature-item">
              <div class="flex-shrink-0 w-12 h-12 rounded-xl bg-gradient-to-br from-blue-500/20 to-blue-600/20 border border-blue-500/30 flex items-center justify-center floating-icon">
                <svg class="w-6 h-6 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                </svg>
              </div>
              <div>
                <h3 class="text-lg font-semibold text-white">Lightning Fast Bidding</h3>
                <p class="text-slate-400">Bid in real-time with instant updates</p>
              </div>
            </div>

            <div class="flex items-start space-x-4 feature-item" style="animation-delay: 0.2s">
              <div class="flex-shrink-0 w-12 h-12 rounded-xl bg-gradient-to-br from-purple-500/20 to-purple-600/20 border border-purple-500/30 flex items-center justify-center floating-icon" style="animation-delay: 0.5s">
                <svg class="w-6 h-6 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                </svg>
              </div>
              <div>
                <h3 class="text-lg font-semibold text-white">Secure Transactions</h3>
                <p class="text-slate-400">Your data is protected with encryption</p>
              </div>
            </div>

            <div class="flex items-start space-x-4 feature-item" style="animation-delay: 0.4s">
              <div class="flex-shrink-0 w-12 h-12 rounded-xl bg-gradient-to-br from-pink-500/20 to-pink-600/20 border border-pink-500/30 flex items-center justify-center floating-icon" style="animation-delay: 1s">
                <svg class="w-6 h-6 text-pink-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <div>
                <h3 class="text-lg font-semibold text-white">Win Amazing Items</h3>
                <p class="text-slate-400">Thousands of items up for auction daily</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Right: Signup Form -->
        <div class="w-full">
          <div class="bg-slate-900/40 backdrop-blur-xl rounded-3xl border border-slate-700/50 p-8 shadow-2xl">
            <div class="text-center mb-8">
              <h2 class="text-3xl font-bold text-white mb-2">Create Account</h2>
              <p class="text-slate-400">Join thousands of happy bidders</p>
            </div>

            <form @submit.prevent="handleSignup" class="space-y-5">
              <!-- Username field -->
              <div>
                <label for="username" class="block text-sm font-medium text-slate-300 mb-2">
                  Username <span class="text-pink-400">*</span>
                </label>
                <input
                  id="username"
                  v-model="formData.username"
                  type="text"
                  required
                  autocomplete="username"
                  placeholder="Choose a unique username"
                  class="w-full px-4 py-3 bg-slate-800/50 border border-slate-700 rounded-xl text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent transition-all"
                />
              </div>

              <!-- Email field -->
              <div>
                <label for="email" class="block text-sm font-medium text-slate-300 mb-2">
                  Email Address <span class="text-pink-400">*</span>
                </label>
                <input
                  id="email"
                  v-model="formData.email"
                  type="email"
                  required
                  autocomplete="email"
                  placeholder="your.email@example.com"
                  class="w-full px-4 py-3 bg-slate-800/50 border border-slate-700 rounded-xl text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent transition-all"
                />
              </div>

              <!-- Date of Birth field -->
              <div>
                <label for="dob" class="block text-sm font-medium text-slate-300 mb-2">
                  Date of Birth <span class="text-pink-400">*</span>
                </label>
                <input
                  id="dob"
                  v-model="formData.date_of_birth"
                  type="date"
                  required
                  class="w-full px-4 py-3 bg-slate-800/50 border border-slate-700 rounded-xl text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent transition-all"
                />
              </div>

              <!-- Password field -->
              <div>
                <label for="password" class="block text-sm font-medium text-slate-300 mb-2">
                  Password <span class="text-pink-400">*</span>
                </label>
                <input
                  id="password"
                  v-model="formData.password"
                  type="password"
                  required
                  minlength="8"
                  autocomplete="new-password"
                  placeholder="Minimum 8 characters"
                  class="w-full px-4 py-3 bg-slate-800/50 border border-slate-700 rounded-xl text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent transition-all"
                />
              </div>

              <!-- Confirm Password field -->
              <div>
                <label for="confirm_password" class="block text-sm font-medium text-slate-300 mb-2">
                  Confirm Password <span class="text-pink-400">*</span>
                </label>
                <input
                  id="confirm_password"
                  v-model="formData.confirm_password"
                  type="password"
                  required
                  autocomplete="new-password"
                  placeholder="Re-enter your password"
                  class="w-full px-4 py-3 bg-slate-800/50 border border-slate-700 rounded-xl text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent transition-all"
                />
              </div>

              <!-- Error display -->
              <div v-if="error" class="p-4 bg-red-500/20 border border-red-500/50 rounded-xl">
                <div class="flex items-start space-x-3">
                  <svg class="w-5 h-5 text-red-400 flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd" />
                  </svg>
                  <p class="text-red-300 text-sm font-medium">{{ error }}</p>
                </div>
              </div>

              <!-- Submit button -->
              <button
                type="submit"
                :disabled="loading"
                class="w-full bg-gradient-to-r from-blue-600 via-purple-600 to-pink-600 hover:from-blue-500 hover:via-purple-500 hover:to-pink-500 text-white font-semibold py-3 rounded-xl transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center space-x-2 shadow-lg shadow-purple-500/50"
              >
                <span v-if="loading">Creating account...</span>
                <template v-else>
                  <span>Create Account</span>
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6" />
                  </svg>
                </template>
              </button>
            </form>

            <!-- Footer links -->
            <div class="mt-6 text-center">
              <p class="text-slate-400">
                Already have an account?
                <router-link to="/login" class="text-purple-400 hover:text-purple-300 font-semibold transition-colors ml-1">
                  Sign in
                </router-link>
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { useRouter } from 'vue-router';

export default defineComponent({
  name: 'SignupPage',
  setup() {
    const router = useRouter();
    
    const formData = ref({
      username: '',
      email: '',
      password: '',
      confirm_password: '',
      date_of_birth: '',
    });
    
    const loading = ref(false);
    const error = ref('');

    const handleSignup = async () => {
      if (formData.value.password !== formData.value.confirm_password) {
        error.value = 'Passwords do not match';
        return;
      }

      loading.value = true;
      error.value = '';

      try {
        const response = await fetch('/api/auth/signup/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          credentials: 'include',
          body: JSON.stringify({
            username: formData.value.username,
            email: formData.value.email,
            password: formData.value.password,
            date_of_birth: formData.value.date_of_birth,
          }),
        });

        const data = await response.json();

        if (data.ok) {
          // User needs to explicitly log in after creating account
          await router.push('/login');
        } else {
          error.value = data.error || 'Signup failed';
        }
      } catch (err) {
        error.value = 'An error occurred. Please try again.';
        console.error(err);
      } finally {
        loading.value = false;
      }
    };

    return {
      formData,
      loading,
      error,
      handleSignup,
    };
  },
});
</script>

<style scoped>
/* Particle animations */
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
  animation-delay: 0s;
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
  width: 7px;
  height: 7px;
  top: 55%;
  right: 15%;
  animation-duration: 19s;
  animation-delay: 5s;
}

.particle-7 {
  width: 3px;
  height: 3px;
  top: 15%;
  right: 45%;
  animation-duration: 21s;
  animation-delay: 2.5s;
}

.particle-8 {
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

/* Floating geometric shapes */
.floating-shape {
  position: absolute;
  border: 2px solid rgba(147, 51, 234, 0.3);
  animation: shapeFloat 15s infinite ease-in-out;
}

.shape-1 {
  width: 120px;
  height: 120px;
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
  width: 100px;
  height: 100px;
  bottom: 20%;
  left: 20%;
  border-radius: 50% 50% 20% 20%;
  background: linear-gradient(135deg, rgba(147, 51, 234, 0.1) 0%, rgba(59, 130, 246, 0.1) 100%);
  animation-duration: 22s;
  animation-delay: 4s;
}

.shape-4 {
  width: 90px;
  height: 90px;
  top: 30%;
  right: 25%;
  border-radius: 20% 50% 50% 20%;
  background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(236, 72, 153, 0.1) 100%);
  animation-duration: 19s;
  animation-delay: 1s;
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

/* Feature items fade-in animation */
.feature-item {
  animation: fadeInUp 0.8s ease-out forwards;
  opacity: 0;
}

@keyframes fadeInUp {
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
