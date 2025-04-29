<template>
  <div id="app">
    <ChatBot />
  </div>
</template>

<script setup>
import ChatBot from "./components/ChatBot.vue";
</script>

<style>
body {
  font-family: 'Segoe UI', Arial, sans-serif;
  background: #f5f6fa;
  margin: 0;
  padding: 0;
}
#app {
  min-height: 100vh;
}
</style>
