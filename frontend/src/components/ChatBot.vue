<template>
  <div class="chatbot">
    <h2>AI Code Assistant</h2>
    <form @submit.prevent="handleSubmit">
      <input
        v-model="repoUrl"
        type="text"
        placeholder="Nhập URL GitHub repo (public)"
        required
      />
      <textarea
        v-model="question"
        placeholder="Nhập câu hỏi về mã nguồn..."
        required
      ></textarea>
      <button type="submit" :disabled="loading">Gửi</button>
    </form>
    <div class="response" v-if="response">
      <h3>Phản hồi từ AI:</h3>
      <pre>{{ response }}</pre>
    </div>
    <div v-if="loading">Đang xử lý...</div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const repoUrl = ref("");
const question = ref("");
const response = ref("");
const loading = ref(false);

const handleSubmit = async () => {
  loading.value = true;
  response.value = "";
  try {
    const res = await fetch("http://localhost:8000/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        repo_url: repoUrl.value,
        question: question.value,
      }),
    });
    const data = await res.json();
    response.value = data.answer;
  } catch (e) {
    response.value = "Lỗi kết nối backend hoặc backend chưa chạy.";
  }
  loading.value = false;
};
</script>

<style scoped>
.chatbot {
  max-width: 500px;
  margin: 40px auto;
  padding: 24px;
  border: 1px solid #eee;
  border-radius: 8px;
  background: #fafbfc;
}
input,
textarea {
  width: 100%;
  margin-bottom: 12px;
  padding: 8px;
  border-radius: 4px;
  border: 1px solid #ccc;
}
button {
  padding: 8px 16px;
  border-radius: 4px;
  background: #42b983;
  color: #fff;
  border: none;
  cursor: pointer;
}
button:disabled {
  background: #aaa;
}
.response {
  margin-top: 24px;
  background: #f6f8fa;
  padding: 12px;
  border-radius: 4px;
}
</style>
