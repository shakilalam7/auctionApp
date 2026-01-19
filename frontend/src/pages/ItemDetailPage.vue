<template>
  <div class="min-h-screen bg-gradient-to-br from-slate-950 via-indigo-950 to-purple-950 relative overflow-hidden">
    <!-- Animated particles background -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
      <div class="particle particle-1"></div>
      <div class="particle particle-2"></div>
      <div class="particle particle-3"></div>
      <div class="particle particle-4"></div>
      <div class="particle particle-5"></div>
    </div>

    <!-- Updated header styling with glassmorphic effect -->
    <header class="bg-slate-900/50 backdrop-blur-md border-b border-slate-700/50 sticky top-0 z-50 shadow-sm">
      <div class="container mx-auto px-4 py-4">
        <div class="flex items-center justify-between">
          <div class="flex items-center space-x-4">
            <button @click="goBack" class="flex items-center text-slate-400 hover:text-white font-medium transition-colors">
              <svg class="w-5 h-5 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
              </svg>
              Back
            </button>
            <h1 class="text-2xl font-bold text-white">
              Item Details
            </h1>
          </div>
          <router-link to="/home" class="text-purple-400 hover:text-purple-300 font-medium transition-colors">
            ← Back to Dashboard
          </router-link>
        </div>
      </div>
    </header>

    <main class="container mx-auto px-4 py-12 relative z-10">
      <!-- Added loading state -->
      <div v-if="loading" class="text-center py-12">
        <div class="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-purple-500"></div>
        <p class="text-slate-400 mt-4">Loading item...</p>
      </div>

      <div v-else-if="item" class="grid grid-cols-1 lg:grid-cols-2 gap-12">
        <!-- Enhanced image display -->
        <div class="bg-slate-900/70 backdrop-blur-sm border border-slate-800/50 rounded-2xl shadow-xl overflow-hidden">
          <div class="aspect-square bg-slate-800/50 flex items-center justify-center overflow-hidden">
            <img
              v-if="item.image_url"
              :src="item.image_url"
              :alt="item.title"
              class="w-full h-full object-cover"
            />
            <svg
              v-else
              class="w-32 h-32 text-slate-600"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"
              />
            </svg>
          </div>
        </div>

        <!-- Bidding interface -->
        <div class="space-y-6">
          <div>
            <h1 class="text-4xl font-bold text-white mb-3">{{ item.title }}</h1>
            <div class="inline-block bg-red-600/20 text-red-400 text-xs font-bold px-3 py-1 rounded-full border border-red-500/50">
              LIVE AUCTION
            </div>
          </div>
          
          <div class="bg-gradient-to-br from-blue-600 via-purple-600 to-pink-600 rounded-2xl p-8 text-white shadow-2xl">
            <div class="mb-6">
              <span class="text-blue-100 text-sm font-medium uppercase tracking-wide">Current Price</span>
              <div class="flex items-baseline mt-2">
                <span class="text-6xl font-bold">${{ item.current_price }}</span>
              </div>
            </div>
            
            <div class="grid grid-cols-2 gap-4 mb-6 text-sm">
              <div class="bg-white/10 backdrop-blur-sm rounded-lg p-3">
                <p class="text-blue-100 mb-1">Starting Price</p>
                <p class="text-white font-bold text-lg">${{ item.starting_price }}</p>
              </div>
              <div class="bg-white/10 backdrop-blur-sm rounded-lg p-3">
                <p class="text-blue-100 mb-1">Auction Ends</p>
                <p class="text-white font-bold text-lg">{{ formatEndDate(item.ends_at) }}</p>
              </div>
            </div>

            <!-- Bid form -->
            <form @submit.prevent="placeBid" class="space-y-4">
              <div>
                <label for="bid" class="block text-sm font-medium text-blue-100 mb-2">
                  Place Your Bid (min: ${{ (parseFloat(item.current_price) + 0.01).toFixed(2) }})
                </label>
                <input
                  id="bid"
                  v-model.number="bidAmount"
                  type="number"
                  :min="parseFloat(item.current_price) + 0.01"
                  step="0.01"
                  required
                  class="w-full px-4 py-4 bg-white/95 border-2 border-white/50 rounded-xl text-gray-900 font-bold text-xl focus:outline-none focus:ring-2 focus:ring-white focus:border-transparent"
                />
              </div>

              <button
                type="submit"
                :disabled="bidding"
                class="w-full bg-white text-purple-600 font-bold py-4 px-6 rounded-xl hover:bg-gray-50 transition-all duration-300 shadow-lg disabled:opacity-50 disabled:cursor-not-allowed"
              >
                {{ bidding ? 'Placing Bid...' : 'Place Bid Now' }}
              </button>
            </form>

            <div v-if="bidError" class="mt-4 p-4 bg-red-500/20 border border-red-300 rounded-lg backdrop-blur-sm">
              <p class="text-white font-medium">{{ bidError }}</p>
            </div>
            <div v-if="bidSuccess" class="mt-4 p-4 bg-green-500/20 border border-green-300 rounded-lg backdrop-blur-sm">
              <p class="text-white font-medium">Bid placed successfully!</p>
            </div>
          </div>

          <!-- Description card -->
          <div class="bg-slate-900/70 backdrop-blur-sm border border-slate-800/50 rounded-2xl p-8">
            <h2 class="text-2xl font-bold text-white mb-4 flex items-center">
              <svg class="w-6 h-6 mr-2 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              Description
            </h2>
            <p class="text-slate-300 leading-relaxed text-lg">{{ item.description }}</p>
          </div>

          <!-- Seller info -->
          <div class="bg-slate-900/70 backdrop-blur-sm border border-slate-800/50 rounded-2xl p-8">
            <h2 class="text-2xl font-bold text-white mb-4">Seller Information</h2>
            <div class="flex items-center space-x-4">
              <div class="w-12 h-12 bg-gradient-to-br from-blue-500 via-purple-500 to-pink-500 rounded-full flex items-center justify-center text-white font-bold text-lg">
                {{ item.owner.username.charAt(0).toUpperCase() }}
              </div>
              <div>
                <p class="text-white font-bold text-lg">{{ item.owner.username }}</p>
                <p class="text-slate-400 text-sm">Verified Seller</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Q&A section -->
      <div v-if="item" class="mt-12">
        <div class="bg-slate-900/70 backdrop-blur-sm border border-slate-800/50 rounded-2xl p-8">
          <h2 class="text-3xl font-bold text-white mb-8 flex items-center">
            <svg class="w-8 h-8 mr-3 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            Questions & Answers
          </h2>

          <!-- Question form (only show if not the owner) -->
          <form v-if="!isOwner()" @submit.prevent="askQuestion" class="mb-10 bg-slate-800/50 backdrop-blur-sm rounded-xl p-6 border border-slate-700/50">
            <div class="mb-4">
              <label for="question" class="block text-sm font-bold text-slate-300 mb-3">
                Have a question about this item?
              </label>
              <textarea
                id="question"
                v-model="questionText"
                rows="3"
                class="w-full px-4 py-3 bg-slate-900/70 border border-slate-700 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
                placeholder="Ask the seller anything..."
              ></textarea>
            </div>
            
            <!-- Added success message for questions -->
            <div v-if="questionSuccess" class="mb-4 p-4 bg-green-500/20 border border-green-300 rounded-lg backdrop-blur-sm">
              <p class="text-green-300 font-medium">{{ questionSuccess }}</p>
            </div>
            
            <!-- Added error message for questions -->
            <div v-if="questionError" class="mb-4 p-4 bg-red-500/20 border border-red-300 rounded-lg backdrop-blur-sm">
              <p class="text-red-300 font-medium">{{ questionError }}</p>
            </div>
            
            <button
              type="submit"
              :disabled="askingQuestion || !questionText.trim()"
              class="px-8 py-3 bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white font-bold rounded-xl transition-all shadow-lg disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {{ askingQuestion ? 'Posting...' : 'Post Question' }}
            </button>
          </form>

          <!-- Added success message for replies (visible to owner) -->
          <div v-if="replySuccess && isOwner()" class="mb-6 p-4 bg-green-500/20 border border-green-300 rounded-lg backdrop-blur-sm">
            <p class="text-green-300 font-medium">{{ replySuccess }}</p>
          </div>

          <!-- Questions list -->
          <div class="space-y-6">
            <div v-for="q in questions" :key="q.id" class="border-l-4 border-blue-600 pl-6 py-4 bg-slate-800/30 backdrop-blur-sm rounded-r-xl">
              <div class="mb-4">
                <p class="text-white text-lg font-medium mb-2">{{ q.text }}</p>
                <p class="text-slate-400 text-sm flex items-center">
                  <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                  </svg>
                  Asked by {{ q.asker.username }}
                </p>
              </div>
              
              <!-- Existing reply -->
              <div v-if="q.reply" class="ml-6 bg-blue-600/10 backdrop-blur-sm border border-blue-500/30 rounded-lg p-4">
                <p class="text-slate-200 mb-2">{{ q.reply.text }}</p>
                <p class="text-blue-400 text-sm font-medium">Seller's Answer</p>
              </div>
              
              <!-- Reply form for owner -->
              <div v-else-if="isOwner()" class="ml-6">
                <div v-if="replyingTo === q.id" class="bg-slate-800/50 backdrop-blur-sm rounded-lg p-4 border border-slate-700/50">
                  <textarea
                    v-model="replyText"
                    rows="3"
                    class="w-full px-4 py-3 bg-slate-900/70 border border-slate-700 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none mb-3"
                    placeholder="Type your answer..."
                  ></textarea>
                  <div class="flex gap-2">
                    <button
                      @click="submitReply(q.id)"
                      :disabled="!replyText.trim()"
                      class="px-6 py-2 bg-blue-600 hover:bg-blue-700 text-white font-bold rounded-lg transition-all disabled:opacity-50 disabled:cursor-not-allowed"
                    >
                      Submit Reply
                    </button>
                    <button
                      @click="replyingTo = null; replyText = ''"
                      class="px-6 py-2 bg-slate-700 hover:bg-slate-600 text-white font-medium rounded-lg transition-all"
                    >
                      Cancel
                    </button>
                  </div>
                </div>
                <button
                  v-else
                  @click="replyingTo = q.id"
                  class="px-6 py-2 bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white font-bold rounded-lg transition-all shadow-md"
                >
                  Reply to Question
                </button>
              </div>
              
              <!-- Waiting message for non-owners -->
              <div v-else class="ml-6 bg-slate-800/50 backdrop-blur-sm rounded-lg p-4">
                <p class="text-slate-500 italic">Waiting for seller's response...</p>
              </div>
            </div>

            <div v-if="questions.length === 0" class="text-center py-12">
              <svg class="w-16 h-16 text-slate-600 mx-auto mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
            </svg>
              <p class="text-slate-400 font-medium">No questions yet</p>
              <p class="text-slate-500 text-sm mt-1">Be the first to ask!</p>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useAuthStore } from '../stores/auth';
import { fetchWithCsrf } from '../utils/csrf';
import type { Item, Question } from '../types.ts';

interface BidResponse {
  ok: boolean;
  error?: string;
  bid?: {
    id: number;
    amount: string;
    item_id: number;
  };
}

interface QuestionResponse {
  ok: boolean;
  question?: Question;
  error?: string;
}

interface ReplyResponse {
  ok: boolean;
  error?: string;
}

export default defineComponent({
  name: 'ItemDetailPage',
  setup() {
    const route = useRoute();
    const router = useRouter();
    const authStore = useAuthStore();
    
    const item = ref<Item | null>(null);
    const loading = ref(true);
    
    const bidAmount = ref(0);
    const bidding = ref(false);
    const bidError = ref('');
    const bidSuccess = ref(false);
    
    const questionText = ref('');
    const askingQuestion = ref(false);
    const questions = ref<Question[]>([]);
    const replyingTo = ref<number | null>(null);
    const replyText = ref('');

    const questionSuccess = ref('');
    const replySuccess = ref('');
    const questionError = ref('');

    const fetchItem = async () => {
      loading.value = true;
      try {
        const response = await fetch(`/api/items/${route.params.id}/`, {
          credentials: 'include',
        });

        if (response.ok) {
          const data = await response.json();
          item.value = data.item;
          bidAmount.value = parseFloat(data.item.current_price) + 1;
        }
      } catch (error) {
        console.error('Failed to fetch item:', error);
      } finally {
        loading.value = false;
      }
    };

    const fetchQuestions = async () => {
      try {
        const response = await fetch(`/api/items/${route.params.id}/questions/`, {
          credentials: 'include',
        });

        if (response.ok) {
          const data = await response.json();
          questions.value = data.questions || [];
        }
      } catch (error) {
        console.error('Failed to fetch questions:', error);
      }
    };

    const placeBid = async () => {
      bidding.value = true;
      bidError.value = '';
      bidSuccess.value = false;

      try {
        const data = await fetchWithCsrf(`/api/items/${route.params.id}/bids/`, {
          method: 'POST',
          body: JSON.stringify({ amount: bidAmount.value }),
        }) as BidResponse;

        if (data.ok) {
          bidSuccess.value = true;
          await fetchItem();
          bidAmount.value = parseFloat(item.value!.current_price) + 1;
        } else {
          bidError.value = data.error || 'Failed to place bid';
        }
      } catch (error) {
        bidError.value = 'An error occurred. Please try again.';
        console.error(error);
      } finally {
        bidding.value = false;
      }
    };

    const askQuestion = async () => {
      if (!questionText.value.trim()) return;

      askingQuestion.value = true;
      questionSuccess.value = '';
      questionError.value = '';

      try {
        const data = await fetchWithCsrf(`/api/items/${route.params.id}/questions/`, {
          method: 'POST',
          body: JSON.stringify({ text: questionText.value }),
        }) as QuestionResponse;

        if (data.ok) {
          // Add the question to the list if returned, otherwise refetch
          if (data.question) {
            questions.value.unshift(data.question);
          } else {
            await fetchQuestions();
          }
          questionText.value = '';
          questionSuccess.value = 'Your question has been sent to the seller successfully!';
          // Clear success message after 5 seconds
          setTimeout(() => {
            questionSuccess.value = '';
          }, 5000);
        } else {
          questionError.value = data.error || 'Failed to post question. Please try again.';
        }
      } catch (error) {
        console.error('Failed to ask question:', error);
        questionError.value = 'An error occurred. Please try again.';
      } finally {
        askingQuestion.value = false;
      }
    };

    const submitReply = async (questionId: number) => {
      if (!replyText.value.trim()) return;

      try {
        const data = await fetchWithCsrf(`/api/questions/${questionId}/reply/`, {
          method: 'POST',
          body: JSON.stringify({ text: replyText.value }),
        }) as ReplyResponse;

        if (data.ok) {
          await fetchQuestions();
          replyText.value = '';
          replyingTo.value = null;
          replySuccess.value = 'Your reply has been posted successfully!';
          setTimeout(() => {
            replySuccess.value = '';
          }, 5000);
        }
      } catch (error) {
        console.error('Failed to reply:', error);
      }
    };

    const formatEndDate = (dateString: string) => {
      const date = new Date(dateString);
      return date.toLocaleDateString() + ' ' + date.toLocaleTimeString();
    };

    const goBack = () => {
      router.go(-1);
    };

    const isOwner = () => {
      return item.value && authStore.user && item.value.owner.id === authStore.user.id;
    };

    onMounted(() => {
      fetchItem();
      fetchQuestions();
    });

    return {
      item,
      loading,
      bidAmount,
      bidding,
      bidError,
      bidSuccess,
      questionText,
      askingQuestion,
      questions,
      replyingTo,
      replyText,
      questionSuccess,
      replySuccess,
      questionError,
      placeBid,
      askQuestion,
      submitReply,
      formatEndDate,
      goBack,
      isOwner,
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
  top: 10%;
  left: 15%;
  animation-duration: 18s;
}

.particle-2 {
  width: 6px;
  height: 6px;
  top: 60%;
  right: 20%;
  animation-duration: 22s;
  animation-delay: 2s;
}

.particle-3 {
  width: 5px;
  height: 5px;
  top: 30%;
  right: 10%;
  animation-duration: 20s;
  animation-delay: 4s;
}

.particle-4 {
  width: 4px;
  height: 4px;
  bottom: 20%;
  left: 25%;
  animation-duration: 19s;
  animation-delay: 1s;
}

.particle-5 {
  width: 5px;
  height: 5px;
  top: 80%;
  left: 60%;
  animation-duration: 21s;
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
</style>
