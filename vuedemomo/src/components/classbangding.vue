<template>
  <div class="classbangding">
    <h3>class绑定</h3>
    <p :class="myClass">asa</p >
    <h5>动态绑定对象实例</h5>
    <p :class="{ active: isActive, 'text-danger': hasError }">class绑定样式1</p >
    <div :class="classObject">class绑定样式2</div>
    <h5>绑定数组示例</h5>
    <p :class="arrActive">class绑定样式3</p >
    <p :class="[isActive ? 'active' : '']">class绑定样式4</p >
    <!-- 数组和对象一起使用嵌套中，只能是数组嵌套对象，对象嵌套数组无效 -->
    <p :class="[isActive ? 'active' : '', { 'text-danger': hasError }]">class绑定5</p >
  </div>
</template>

<script>
export default {
  name: "12classbangding",
  data() {
    return {
      myClass: "demo",
      isActive: true,
      hasError: false,
      hasError: true,
      classObject: {
        active: true,
        "text-danger": true,
      },
      arrActive: "active",
      arrHasError: "text-danger",
    };
  },
};
</script>

<style scoped>
.classbangding {
  color: teal;
}
.active {
  font-size: 35px;
}
.text-danger {
  color: red;
}
</style>