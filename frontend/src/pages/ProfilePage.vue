<template>
  <div class="min-h-screen bg-slate-950">
    <!-- Header -->
    <header class="bg-slate-900 border-b border-slate-800">
      <div class="container mx-auto px-4 py-4">
        <div class="flex items-center space-x-4">
          <router-link
            to="/home"
            class="flex items-center text-slate-400 hover:text-white font-medium transition-colors"
          >
            <svg class="w-5 h-5 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M15 19l-7-7 7-7"
              />
            </svg>
            Back to Dashboard
          </router-link>
          <h1 class="text-2xl font-bold text-white">
            My Profile
          </h1>
        </div>
      </div>
    </header>

    <main class="container mx-auto px-4 py-12 max-w-3xl">
      <div class="text-center mb-12">
        <h1 class="text-5xl font-bold text-white mb-4">My Profile</h1>
        <p class="text-xl text-slate-400">Manage your account settings</p>
      </div>

      <!-- Added loading state -->
      <div v-if="loading" class="text-center py-12">
        <div class="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-purple-500"></div>
        <p class="text-slate-400 mt-4">Loading profile...</p>
      </div>

      <div v-else class="bg-slate-900 border border-slate-800 rounded-2xl shadow-2xl overflow-hidden">
        <!-- Avatar -->
        <div class="bg-gradient-to-r from-blue-600 to-purple-600 p-8 text-center">
          <div
            class="w-32 h-32 mx-auto mb-4 bg-white rounded-full flex items-center justify-center overflow-hidden ring-4 ring-white/50"
          >
            <img
              v-if="user?.profile_image_url"
              :src="user.profile_image_url"
              alt="Profile"
              class="w-full h-full object-cover"
            />
            <div
              v-else
              class="w-full h-full bg-gradient-to-br from-blue-400 to-purple-400 flex items-center justify-center text-white text-4xl font-bold"
            >
              {{ user?.username.charAt(0).toUpperCase() }}
            </div>
          </div>

          <h2 class="text-3xl font-bold text-white mb-2">
            {{ user?.username }}
          </h2>

          <p class="text-blue-100">
            {{ user?.email }}
          </p>
        </div>

        <!-- Form -->
        <div class="p-10">
          <form @submit.prevent="updateProfile" class="space-y-6">
            <div>
              <label class="block text-sm font-bold text-slate-300 mb-2">
                Email Address
              </label>
              <input
                v-model="formData.email"
                type="email"
                required
                class="w-full px-4 py-4 bg-slate-800/50 border border-slate-700 rounded-xl text-white"
              />
            </div>

            <div>
              <label class="block text-sm font-bold text-slate-300 mb-2">
                Date of Birth
              </label>
              <input
                v-model="formData.date_of_birth"
                type="date"
                class="w-full px-4 py-4 bg-slate-800/50 border border-slate-700 rounded-xl text-white"
              />
            </div>

            <div>
              <label class="block text-sm font-bold text-slate-300 mb-2">
                Profile Picture
              </label>
              <input type="file" accept="image/*" @change="handleImageUpload" class="text-slate-300" />
            </div>

            <div v-if="error" class="text-red-400 font-medium">
              {{ error }}
            </div>

            <div v-if="success" class="text-green-400 font-medium">
              Profile updated successfully!
            </div>

            <button
              type="submit"
              :disabled="updating"
              class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-4 rounded-xl disabled:opacity-50 transition-all"
            >
              {{ updating ? "Saving..." : "Save Changes" }}
            </button>
          </form>
        </div>
      </div>
    </main>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from "vue"
import { useAuthStore } from "../stores/auth"
import { fetchWithCsrf } from "../utils/csrf"

export default defineComponent({
  name: "ProfilePage",
  setup() {
    const authStore = useAuthStore()

    const user = ref(authStore.user)
    const loading = ref(true)

    const formData = ref({
      email: "",
      date_of_birth: "",
      profile_image: null as File | null,
    })

    const updating = ref(false)
    const error = ref("")
    const success = ref(false)

    const fetchProfile = async () => {
      loading.value = true
      try {
        await authStore.fetchUser()
        user.value = authStore.user
        if (user.value) {
          formData.value.email = user.value.email
          formData.value.date_of_birth = user.value.date_of_birth || ""
        }
      } catch (err) {
        error.value = "Failed to load profile"
      } finally {
        loading.value = false
      }
    }

    const handleImageUpload = (event: Event) => {
      const target = event.target as HTMLInputElement
      if (target.files && target.files[0]) {
        formData.value.profile_image = target.files[0]
      }
    }

    const updateProfile = async () => {
      updating.value = true
      error.value = ""
      success.value = false

      try {
        const payload = new FormData()
        payload.append("email", formData.value.email)
        if (formData.value.date_of_birth) {
          payload.append("date_of_birth", formData.value.date_of_birth)
        }

        if (formData.value.profile_image) {
          payload.append("profile_image", formData.value.profile_image)
        }

        const response = await fetchWithCsrf("/api/me/", {
          method: "POST",
          body: payload,
        })

        const data = await response.json()

        if (data.ok) {
          await authStore.fetchUser()
          user.value = authStore.user
          success.value = true
          formData.value.profile_image = null
        } else {
          error.value = "Failed to update profile"
        }
      } catch (err) {
        console.error("Profile update error:", err)
        error.value = "Failed to update profile"
      } finally {
        updating.value = false
      }
    }

    onMounted(() => {
      fetchProfile()
    })

    return {
      user,
      loading,
      formData,
      updating,
      error,
      success,
      handleImageUpload,
      updateProfile,
    }
  },
})
</script>
