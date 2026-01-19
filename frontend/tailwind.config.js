/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: "#3b82f6",
        secondary: "#8b5cf6",
      },
      animation: {
        float: "float 25s infinite ease-in-out",
        orbit: "orbit 15s linear infinite",
      },
    },
  },
  plugins: [],
}
