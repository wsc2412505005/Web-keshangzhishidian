<template>
  <div class="home-container" v-if="showContent">
    <h1>Vue教学</h1>
    <nav class="navgation">
      <router-link class="nav-link" to="/new">跳到新组件</router-link>
    </nav>
    <hr>
    <mobanyufa></mobanyufa>
    <shuxingbangding></shuxingbangding>
    <tiaojianxuanran></tiaojianxuanran>
    <liebiaoxuanran></liebiaoxuanran>
    <shijianchuli></shijianchuli>
    <classbangding></classbangding>
  </div>
</template>

<script>
import mobanyufa from "../components/mobanyufa.vue";
import shuxingbangding from "../components/shuxingbangding.vue";
import tiaojianxuanran from "../components/tiaojianxuanran.vue";
import liebiaoxuanran from "../components/liebiaoxuanran.vue";
import shijianchuli from "../components/shijianchuli.vue";
import Classbangding from "../components/classbangding.vue";
import classbangding from "../components/classbangding.vue";
import router from "../router/router.js";


export default {
  name: "Home",
  components: {
    mobanyufa,
    shuxingbangding,
    tiaojianxuanran,
    liebiaoxuanran,
    shijianchuli,
    classbangding

  },
  data() {
    return {
      showContent: false,
    };
  },
  methods: {},
  mounted() {
    setTimeout(() => {
      this.showContent = true;
    }, 0);
  },
};
</script>

<style scoped>
.home-container {
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
