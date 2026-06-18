<template>
  <div class="new-container" v-if="showContent">
    <h1>new 组件集合</h1>
    <nav class="navigation">
      <router-link class="nav-link" to="/">返回首页</router-link>
    </nav>
    <hr>
  </div>
</template>

<script>
export default {
  name: "new",
  data() {
    return {
      showContent: false,
    };
  },
  mounted() {
    setTimeout(() => {
      this.showContent = true;
    }, 0);
  },
};
</script>

<style scoped>
.new-container {
  position: relative;
  z-index: 10;
}

h1 {
  z-index: 11;
  color: white;
}

.navigation {
  margin: 20px 0;
  z-index: 11;
}

.nav-link {
  display: inline-block;
  padding: 10px 20px;
  background-color: rgba(255, 255, 255, 0.1);
  color: white;
  text-decoration: none;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.nav-link:hover {
  background-color: rgba(255, 255, 255, 0.2);
}
</style>