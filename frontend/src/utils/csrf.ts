export function getCsrfToken(): string | null {
    const name = "csrftoken"
    let cookieValue: string | null = null
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";")
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim()
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
          break
        }
      }
    }
    return cookieValue
  }
  
  export async function fetchWithCsrf(url: string, options: RequestInit = {}): Promise<Response> {
    const csrfToken = getCsrfToken()
  
    const headers = new Headers(options.headers || {})
    if (
      csrfToken &&
      (options.method === "POST" || options.method === "PUT" || options.method === "PATCH" || options.method === "DELETE")
    ) {
      headers.set("X-CSRFToken", csrfToken)
    }
  
    return fetch(url, {
      ...options,
      headers,
      credentials: "include",
    })
  }
  