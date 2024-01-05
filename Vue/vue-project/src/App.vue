<template>
  <div>
    <HomeView />
  </div>
  <RouterView />
</template>

<script setup>
import HomeView from '@/views/HomeView.vue'
import { RouterView, RouterLink } from 'vue-router'
</script>

<style scoped>

</style>
