<template>
  <div class="chart-card">
    <h3>地域风险评级多维对比</h3>
    <div ref="chartRef" class="chart-container"></div>
  </div>
</template>

<script setup>
import { onMounted, onBeforeUnmount, ref, watch } from 'vue'
import * as echarts from 'echarts'

const props = defineProps({
  data: {
    type: Array,
    required: true, // 结构：[{ region: '海南自贸港', high: 2, medium: 1, low: 4 }]
  },
})

const chartRef = ref(null)
let chartInstance = null
let resizeObserver = null

const initChart = () => {
  if (!chartRef.value) return

  chartInstance = echarts.init(chartRef.value, 'dark')

  const regions = props.data.map(item => item.region)
  const maxVal = Math.max(...props.data.flatMap(item => [item.high, item.medium, item.low]), 3)

  const option = {
    backgroundColor: 'transparent',
    tooltip: {
      trigger: 'item',
      backgroundColor: 'rgba(20, 20, 20, 0.88)',
      borderColor: 'rgba(255, 255, 255, 0.1)',
      borderWidth: 1,
      textStyle: {
        color: '#ffffff',
        fontSize: 12,
        fontFamily: 'inherit',
      },
    },
    legend: {
      data: ['高风险', '中风险', '低风险'],
      bottom: '0%',
      icon: 'circle',
      textStyle: {
        color: 'rgba(255, 255, 255, 0.65)',
        fontSize: 11,
      },
      itemGap: 20,
    },
    radar: {
      indicator: regions.map(name => ({ name, max: maxVal })),
      center: ['50%', '45%'],
      radius: '62%',
      shape: 'polygon',
      axisName: {
        color: 'rgba(255, 255, 255, 0.72)',
        fontSize: 11,
        fontFamily: 'inherit',
      },
      splitArea: {
        show: true,
        areaStyle: {
          color: ['rgba(255, 255, 255, 0.01)', 'rgba(255, 255, 255, 0.02)'],
        },
      },
      splitLine: {
        lineStyle: {
          color: 'rgba(255, 255, 255, 0.06)',
        },
      },
      axisLine: {
        lineStyle: {
          color: 'rgba(255, 255, 255, 0.06)',
        },
      },
    },
    series: [
      {
        name: '地域风险评级',
        type: 'radar',
        symbol: 'circle',
        symbolSize: 4,
        data: [
          {
            value: props.data.map(item => item.high),
            name: '高风险',
            itemStyle: { color: '#f0a08d' },
            lineStyle: { width: 2 },
            areaStyle: {
              color: 'rgba(240, 160, 141, 0.12)',
            },
          },
          {
            value: props.data.map(item => item.medium),
            name: '中风险',
            itemStyle: { color: '#e2c581' },
            lineStyle: { width: 2 },
            areaStyle: {
              color: 'rgba(226, 197, 129, 0.12)',
            },
          },
          {
            value: props.data.map(item => item.low),
            name: '低风险',
            itemStyle: { color: '#93d0bd' },
            lineStyle: { width: 2 },
            areaStyle: {
              color: 'rgba(147, 208, 189, 0.12)',
            },
          },
        ],
      },
    ],
  }

  chartInstance.setOption(option)
}

watch(
  () => props.data,
  (newData) => {
    if (chartInstance) {
      const maxVal = Math.max(...newData.flatMap(item => [item.high, item.medium, item.low]), 3)
      chartInstance.setOption({
        radar: {
          indicator: newData.map(item => ({ name: item.region, max: maxVal })),
        },
        series: [
          {
            data: [
              { value: newData.map(item => item.high), name: '高风险' },
              { value: newData.map(item => item.medium), name: '中风险' },
              { value: newData.map(item => item.low), name: '低风险' },
            ],
          },
        ],
      })
    }
  },
  { deep: true },
)

onMounted(() => {
  initChart()

  if (window.ResizeObserver && chartRef.value) {
    resizeObserver = new ResizeObserver(() => {
      chartInstance?.resize()
    })
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
