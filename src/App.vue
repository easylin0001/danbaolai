<template>
  <div class="app-container">
    <UserPage />
  </div>
</template>

<script setup lang="ts">
import UserPage from '@/views/user/index.vue'
</script>

<style scoped>
.app-container {
  min-height: 100vh;
  background-color: #f5f7fa;
}
</style>
