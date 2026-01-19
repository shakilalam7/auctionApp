import { createRouter, createWebHistory, type RouteRecordRaw } from "vue-router"
import SignupPage from "../pages/SignupPage.vue"
import LoginPage from "../pages/LoginPage.vue"
import HomePage from "../pages/HomePage.vue"
import ProfilePage from "../pages/ProfilePage.vue"
import BrowseAuctionsPage from "../pages/BrowseAuctionsPage.vue"
import CreateItemPage from "../pages/CreateItemPage.vue"
import ItemDetailPage from "../pages/ItemDetailPage.vue"
import MessagesPage from "../pages/MessagesPage.vue"
import MyBidsPage from "../pages/MyBidsPage.vue"
import MyAuctionsPage from "../pages/MyAuctionsPage.vue"
import NotificationsPage from "../pages/NotificationsPage.vue"
import SettingsPage from "../pages/SettingsPage.vue"
import { useAuthStore } from "../stores/auth"

const routes: RouteRecordRaw[] = [
  {
    path: "/",
    redirect: "/signup",
  },
  {
    path: "/signup",
    name: "Signup",
    component: SignupPage,
    meta: { requiresGuest: true },
  },
  {
    path: "/login",
    name: "Login",
    component: LoginPage,
    meta: { requiresGuest: true },
  },
  {
    path: "/home",
    name: "Home",
    component: HomePage,
    meta: { requiresAuth: true },
  },
  {
    path: "/profile",
    name: "Profile",
    component: ProfilePage,
    meta: { requiresAuth: true },
  },
  {
    path: "/browse",
    name: "BrowseAuctions",
    component: BrowseAuctionsPage,
    meta: { requiresAuth: true },
  },
  {
    path: "/create",
    name: "CreateItem",
    component: CreateItemPage,
    meta: { requiresAuth: true },
  },
  {
    path: "/item/:id",
    name: "ItemDetail",
    component: ItemDetailPage,
    meta: { requiresAuth: true },
  },
  {
    path: "/messages",
    name: "Messages",
    component: MessagesPage,
    meta: { requiresAuth: true },
  },
  {
    path: "/my-bids",
    name: "MyBids",
    component: MyBidsPage,
    meta: { requiresAuth: true },
  },
  {
    path: "/my-auctions",
    name: "MyAuctions",
    component: MyAuctionsPage,
    meta: { requiresAuth: true },
  },
  {
    path: "/notifications",
    name: "Notifications",
    component: NotificationsPage,
    meta: { requiresAuth: true },
  },
  {
    path: "/settings",
    name: "Settings",
    component: SettingsPage,
    meta: { requiresAuth: true },
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

let authInitialized = false

router.beforeEach(async (to, _from, next) => {
  const authStore = useAuthStore()

  if (!authInitialized) {
    authInitialized = true
    await authStore.fetchUser()
  }

  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next("/signup")
  } else if (to.meta.requiresGuest && authStore.isAuthenticated) {
    next("/home")
  } else {
    next()
  }
})

export default router
