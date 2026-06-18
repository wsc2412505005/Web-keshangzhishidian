<template>
  <div class="chart-card">
    <h3>合规主题类别分布</h3>
    <div ref="chartRef" class="chart-container"></div>
  </div>
</template>

<script setup>
import { onMounted, onBeforeUnmount, ref, watch } from 'vue'
import * as echarts from 'echarts'

const props = defineProps({
  data: {
    type: Array,
    required: true,
  },
})

const chartRef = ref(null)
let chartInstance = null
let resizeObserver = null

const initChart = () => {
  if (!chartRef.value) return

  chartInstance = echarts.init(chartRef.value, 'dark')

  const option = {
    backgroundColor: 'transparent',
    tooltip: {
      trigger: 'item',
      formatter: '{b} : {c} 篇 ({d}%)',
      backgroundColor: 'rgba(20, 20, 20, 0.88)',
      borderColor: 'rgba(255, 255, 255, 0.1)',
      borderWidth: 1,
      textStyle: {
        color: '#ffffff',
        fontSize: 12,
        fontFamily: 'inherit',
      },
    },
    series: [
      {
        name: '合规主题',
        type: 'pie',
        radius: ['15%', '70%'],
        center: ['50%', '50%'],
        roseType: 'radius',
        itemStyle: {
          borderRadius: 5,
        },
        label: {
          show: true,
          color: 'rgba(255, 255, 255, 0.72)',
          fontSize: 11,
          formatter: '{b}\n{c}篇',
        },
        labelLine: {
          lineStyle: {
            color: 'rgba(255, 255, 255, 0.16)',
          },
          smooth: 0.2,
          length: 10,
          length2: 12,
        },
        data: props.data,
      },
    ],
    // 调色盘选用和金黑色调一致的深空渐变系
    color: [
      '#c8a866', // 金色
      '#8cc9b5', // 翡翠绿
      '#d3a078', // 浅咖
      '#9fb7ff', // 浅蓝
      '#bba2ff', // 浅紫
      '#e2c581', // 浅黄
      '#f0a08d', // 浅珊瑚红
    ],
  }

  chartInstance.setOption(option)
}

watch(
  () => props.data,
  (newData) => {
    if (chartInstance) {
      chartInstance.setOption({
        series: [{ data: newData }],
      })
    }
  },
  { deep: true },
)

onMounted(() => {
  initChart()

  // 监听容器大小改变自适应
  if (window.ResizeObserver && chartRef.value) {
    resizeObserver = new ResizeObserver(() => {
      chartInstance?.resize()
    })
    // 监听图表外层的容器
    const parent = chartRef.value.parentElement
    if (parent) resizeObserver.observe(parent)
  }
})

onBeforeUnmount(() => {
  resizeObserver?.disconnect()
  chartInstance?.dispose()
})
</script>

<style scoped>
.chart-card {
  padding: clamp(20px, 3vw, 28px);
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.07);
  background: linear-gradient(145deg, rgba(255, 255, 255, 0.025), rgba(255, 255, 255, 0.005)),
              rgba(16, 16, 16, 0.48);
  backdrop-filter: blur(14px);
  box-shadow: var(--shadow-deep);
  display: flex;
  flex-direction: column;
  height: 380px;
}

h3 {
  font-size: 15px;
  font-weight: 900;
  margin: 0 0 16px;
  color: rgba(255, 255, 255, 0.9);
  letter-spacing: 0.05em;
}

.chart-container {
  flex-grow: 1;
  width: 100%;
  height: 100%;
}
</style>
