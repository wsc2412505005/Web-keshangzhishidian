<template>
  <div class="shijianchuli">
    <h3>事件处理</h3>
    <!-- 内联事件处理器 -->
    <button @click="count++">点击我</button>
    <p>点击了 {{ count }} 次</p >

    <!-- 方法事件处理器 -->
    <button @click="handleClick">点击我</button>
    <p>countNum is {{ countNum }}</p >
    <hr>
  </div>
</template>

<script>
export default {
  name: "shijianchuli",
  data() {
    return {
      count: 0,
      countNum: 0,
    };
  },
  methods: {
    handleClick() {
      this.countNum += 3;
      console.log("点击了", this.countNum, "次");
    },
  },
};
</script>

<style scoped>
.shijianchuli {
  color: seagreen;
}
</style>