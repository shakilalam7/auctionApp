<template>
  <router-view />
</template>

<script lang="ts">
import { defineComponent, onMounted, watch } from 'vue';
import { useAuthStore } from './stores/auth';
import { useRouter } from 'vue-router';

export default defineComponent({
  name: 'App',
  setup() {
    const authStore = useAuthStore();
    const router = useRouter();

    onMounted(() => {
      authStore.fetchUser();
    });

    watch(() => authStore.isAuthenticated, (isAuthenticated) => {
      if (!isAuthenticated && router.currentRoute.value.path !== '/signup' && router.currentRoute.value.path !== '/login') {
        router.push('/signup');
      }
    });

    return {};
  },
});
</script>
