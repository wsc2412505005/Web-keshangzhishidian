<template>
  <div class="chart-card">
    <h3>平台安全低风险率</h3>
    <div ref="chartRef" class="chart-container"></div>
  </div>
</template>

<script setup>
import { onMounted, onBeforeUnmount, ref, watch } from 'vue'
import * as echarts from 'echarts'

const props = defineProps({
  value: {
    type: Number,
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
    series: [
      {
        type: 'gauge',
        startAngle: 180,
        endAngle: 0,
        center: ['50%', '75%'],
        radius: '90%',
        min: 0,
        max: 100,
        splitNumber: 5,
        axisLine: {
          lineStyle: {
            width: 8,
            color: [
              [0.3, '#f0a08d'],  // 低于 30% 红色警告
              [0.7, '#e2c581'],  // 中等黄色
              [1, '#93d0bd'],    // 高安全率绿色
            ],
          },
        },
        pointer: {
          icon: 'path://M12.8,0.7l12,20c0.4,0.7,0.2,1.5-0.4,1.9c-0.2,0.1-0.4,0.2-0.6,0.2H1.2c-0.8,0-1.5-0.7-1.5-1.5c0-0.2,0.1-0.4,0.2-0.6l12-20C12,0.1,12.4,0,12.8,0.7z',
          length: '12%',
          width: 8,
          offsetCenter: [0, '-45%'],
          itemStyle: {
            color: 'auto',
          },
        },
        axisTick: {
          length: 12,
          lineStyle: {
            color: 'auto',
            width: 2,
          },
        },
        splitLine: {
          length: 20,
          lineStyle: {
            color: 'auto',
            width: 3,
          },
        },
        axisLabel: {
          color: 'rgba(255, 255, 255, 0.46)',
          fontSize: 11,
          distance: -46,
          formatter: function (value) {
            if (value === 0) return '0%'
            if (value === 50) return '中'
            if (value === 100) return '安全'
            return ''
          },
        },
        title: {
          offsetCenter: [0, '-20%'],
          fontSize: 13,
          fontWeight: '900',
          color: 'rgba(255, 255, 255, 0.5)',
        },
        detail: {
          fontSize: 28,
          fontWeight: '900',
          offsetCenter: [0, '0%'],
          valueAnimation: true,
          formatter: '{value}%',
          color: 'auto',
        },
        data: [
          {
            value: props.value,
            name: '安全级低风险比例',
          },
        ],
      },
    ],
  }

  chartInstance.setOption(option)
}

// 动态修改字号自适应
const clamp = (min, val, max) => {
  return Math.min(Math.max(min, val), max)
}

watch(
  () => props.value,
  (newValue) => {
    if (chartInstance) {
      chartInstance.setOption({
        series: [{ data: [{ value: newValue, name: '安全级低风险比例' }] }],
      })
    }
  },
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
