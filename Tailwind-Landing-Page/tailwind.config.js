/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js,jsx}"],
  theme: {
    extend: {
      fontfamily:{
        playfair:"'Playfair Display' , serif",
        lato : "'Lato', sans-serif",
      }
    },
  },
  plugins: [],
}