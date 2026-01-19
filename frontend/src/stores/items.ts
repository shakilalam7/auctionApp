// Pinia store for auction items
import { defineStore } from "pinia"
import type { Item } from "../types"

interface ItemsState {
  items: Item[]
  currentItem: Item | null
  searchQuery: string
  loading: boolean
}

export const useItemsStore = defineStore("items", {
  state: (): ItemsState => ({
    items: [],
    currentItem: null,
    searchQuery: "",
    loading: false,
  }),

  getters: {
    filteredItems: (state) => {
      if (!state.searchQuery) return state.items

      const query = state.searchQuery.toLowerCase()
      return state.items.filter(
        (item: Item) => item.title.toLowerCase().includes(query) || item.description.toLowerCase().includes(query),
      )
    },
  },

  actions: {
    async fetchItems() {
      this.loading = true
      try {
        const response = await fetch("/api/items")
        if (response.ok) {
          this.items = await response.json()
        }
      } catch (error) {
        console.error("Failed to fetch items:", error)
      } finally {
        this.loading = false
      }
    },

    async fetchItem(id: number) {
      this.loading = true
      try {
        const response = await fetch(`/api/items/${id}`)
        if (response.ok) {
          this.currentItem = await response.json()
        }
      } catch (error) {
        console.error("Failed to fetch item:", error)
      } finally {
        this.loading = false
      }
    },

    setSearchQuery(query: string) {
      this.searchQuery = query
    },
  },
})
