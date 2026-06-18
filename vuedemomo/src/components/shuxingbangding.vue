<template>
  <div class="shuxingbangding">
    <h3>属性动态绑定</h3>
    <p :id="dynamicId" :class="dynamicClass" :title="titleaaa" :aaa="aaa">
      测试测试
    </p>
    <button :disabled="isButtonDisabled">button</button>
    <div v-bind="objectOfattrs">阿萨德阿萨德</div>
    <hr>
  </div>
</template>

<script>
export default {
  name: "Shuxingbangding",
  data() {
    return {
      dynamicId: "id1",
      dynamicClass: "class1",
      titleaaa: "标题111",
      aaa: null,
      isButtonDisabled: false,
      objectOfattrs: {
        class: "id2",
        id: "class1",
      },
    };
  },
};
</script>

<style scoped>
.shuxingbangding {
  color: yellow;
}
.class1 {
  color: red;
}
.id2 {
  color: blue;
}
</style>
