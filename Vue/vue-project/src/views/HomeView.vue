<template>
  <div>
    <h1>HomeView</h1>
    <div v-for="i in paginatedInfo" :key="i.id">
      <RouterLink :to="{ name: 'detail', params: { id: i.id }}">{{ i.title }}</RouterLink>
      <p>{{ i.overview }}</p>
      <img :src="imageLink + i.poster_path" alt="123">
      <p>장르</p>
      <span v-for="genreId in i.genre_ids" :key="genreId" class="genre">
        {{ genreMapping[genreId] }}
      </span>
      <hr>
    </div>
    
    <!-- 페이지네이션 컨트롤 -->
    <div>
      <button v-for="page in totalPages" :key="page" @click="goToPage(page)">
        {{ page }}
      </button>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { onMounted, ref, computed } from 'vue';
import { RouterLink, RouterView } from 'vue-router';

const info = ref([]);
const imageLink = ref('https://image.tmdb.org/t/p/w500');
const itemsPerPage = 2;
const currentPage = ref(1);

onMounted(() => {
  axios({
    method: 'get',
    url: 'https://api.themoviedb.org/3/movie/popular?language=ko-KR&page=1',
    headers: {
      accept: 'application/json',
      Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4ZTc0Y2U3YWEwYWRiMGMxYmU4NmJiZDVhNTc3ZTcxMCIsInN1YiI6IjY1NDA5NTc0NjNlNmZiMDBjNzExOTdhYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.kt1B52JAbv4500GFEaEAfi8cKWwuEVW7pN3G3FS_A_M'
    }
  })
  .then((res) => {
    console.log(res);
    info.value = res.data.results;
  });
});

const genreMapping = {
  28: 'Action',
  12: 'Adventure',
  16: 'Animation',
  35: 'Comedy',
  80: 'Crime',
  99: 'Documentary',
  18: 'Drama',
  10751: 'Family',
  14: 'Fantasy',
  36: 'History',
  27: 'Horror',
  10402: 'Music',
  9648: 'Mystery',
  10749: 'Romance',
  878: 'Science Fiction',
  10770: 'TV Movie',
  53: 'Thriller',
  10752: 'War',
  37: 'Western',
};

// 페이지네이션 계산
const totalPages = computed(() => Math.ceil(info.value.length / itemsPerPage));

// 현재 페이지에 따른 데이터 슬라이싱
const paginatedInfo = computed(() => {
  const startIndex = (currentPage.value - 1) * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;
  return info.value.slice(startIndex, endIndex);
});

// 특정 페이지로 이동
const goToPage = (page) => {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page;
  }
};
</script>

<style scoped>
.genre {
  display: inline-block;
  margin-right: 10px; /* 원하는 간격 설정 */
}
</style>
