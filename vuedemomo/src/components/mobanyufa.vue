<template>
  <div class="mobanyufa">
    <h3>模板语法</h3>
    <p>{{ msg }}</p>
    <p>{{ asd }}</p>
    <div>{{ number + 2 }}</div>
    <!-- {{ 是 v-text 的缩写 }} -->
    <p>{{ ok ? "syxy" : "sbxy" }}</p>
    <div>{{ rawHtml }}</div>
    <div v-html="rawHtml"></div>
    <hr>
  </div>
</template>

<script>
// 选项式api写法
export default {
  name: "Mobanyufa",
  data() {
    return {
      msg: "hello 5555554444445555",
      asd: "asssssss",
      number: 50,
      ok: false,
      rawHtml: "<span style='color: red;'>this is rawHtml</span>",
    };
  },
};
</script>

<style scoped>
.mobanyufa {
  color: green;
}
</style>
