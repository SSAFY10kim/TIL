<template>
  <div>
    <h1>Details</h1>
    {{ id }}
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router';
import { ref } from 'vue';

const route = useRoute();

const id = route.params.id
</script>

<style scoped>

</style>
