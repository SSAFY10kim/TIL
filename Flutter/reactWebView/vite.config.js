import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  // "scripts": {
  //   "dev": "vite --host 127.0.0.1 --port 5173"
  // }
})
