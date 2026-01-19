export interface User {
  id: number
  username: string
  email: string
  date_of_birth: string
  profile_image?: string
  created_at?: string
}

export interface Item {
  id: number
  title: string
  description: string
  starting_price: string
  current_price: string
  image_url?: string
  ends_at: string
  owner: {
    id: number
    username: string
  }
  highest_bid?: Bid
  is_closed?: boolean
  is_active?: boolean
  bid_count?: number
  winner?: User
  final_price?: string
}

export interface Bid {
  id: number
  amount: string
  bidder: {
    id: number
    username: string
  }
  created_at: string
  item_id: number
}

export interface Question {
  id: number
  item_id: number
  asker: {
    id: number
    username: string
  }
  text: string
  created_at: string
  reply?: Reply
}

export interface Reply {
  id: number
  owner: {
    id: number
    username: string
  }
  text: string
  created_at: string
}

export interface Notification {
  id: number
  type: "question" | "reply" | "bid" | "outbid" | "won"
  title: string
  message: string
  link?: string | null
  is_read: boolean
  created_at: string
}

export interface LoginCredentials {
  username: string
  password: string
}

export interface SignupData {
  username: string
  email: string
  password: string
  date_of_birth: string
}
