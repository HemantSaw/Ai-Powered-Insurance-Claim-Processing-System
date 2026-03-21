import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  // if my backend server is not running on 5000 port then do the below.
  // server: {
  //   proxy: {
  //     "/": {
  //       target: "http://localhost:5000",
  //       changeOrigin: true,
  //     }
  //   }
  // },
})
