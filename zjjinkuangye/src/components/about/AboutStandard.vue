<template>
  <section class="about-standard">
    <div class="section-title-area">
      <h2>数据采集与清洗标注标准</h2>
      <p>为确保数据的高可信度与合规分析深度，平台设计了标准化的三步数据处理管线：</p>
    </div>

    <div class="pipeline-grid">
      <div class="pipeline-card">
        <div class="step-num">01</div>
        <h3>公开文本采集 (Sourcing)</h3>
        <p>
          主要从三大信源渠道进行公开文本采集：一是国家级与地方级政策网（如海南自贸港官网）；二是大型跨国矿业公司（如紫金矿业）的可持续发展/ESG年报；三是国际规则制定组织（如OECD负责任供应链指南）。
        </p>
      </div>

      <div class="pipeline-card">
        <div class="step-num">02</div>
        <h3>过滤清洗与归一 (Cleaning)</h3>
        <p>
          过滤剔除冗余的网页格式及无关文本，截取核心关键段落作为“原文节选 (`excerpt`)”，并重新编写百字以内的简短摘要 (`summary`)，建立标准化的 JSON 纯文本结构，确保核心法规的引用准确性。
        </p>
      </div>

      <div class="pipeline-card">
        <div class="step-num">03</div>
        <h3>合规标注与评估 (Annotation)</h3>
        <p>
          根据紫金矿业的跨境投资运营特点，由模拟合规专家团队对文本添加业务阶段与合规主题类别。同时，针对文献的条款要求，给出定性的“合规要点”，并从企业视角撰写风险成因与行动应对建议。
        </p>
      </div>
    </div>
  </section>
</template>

<script setup>
// Static layout component
</script>

<style scoped>
.about-standard {
  margin-bottom: clamp(48px, 7vw, 72px);
}

.section-title-area {
  margin-bottom: clamp(24px, 4vw, 36px);
}

.section-title-area h2 {
  font-size: clamp(20px, 2.4vw, 26px);
  font-weight: 900;
  margin: 0 0 8px;
  color: var(--color-text, #ffffff);
}

.section-title-area p {
  font-size: 14px;
  color: var(--color-muted, #8e8e93);
  margin: 0;
}

.pipeline-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: clamp(20px, 2.6vw, 32px);
}

.pipeline-card {
  position: relative;
  padding: 30px;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.06);
  background: linear-gradient(145deg, rgba(255, 255, 255, 0.02), rgba(255, 255, 255, 0.005)),
              rgba(18, 18, 18, 0.5);
  backdrop-filter: blur(12px);
  box-shadow: var(--shadow-deep);
  transition: transform 0.3s var(--ease-premium), border-color 0.3s var(--ease-premium);
}

.pipeline-card:hover {
  transform: translateY(-3px);
  border-color: rgba(200, 168, 102, 0.22);
}

.step-num {
  font-size: clamp(32px, 3.6vw, 44px);
  font-weight: 950;
  line-height: 1;
  color: rgba(200, 168, 102, 0.12);
  margin-bottom: 12px;
  font-family: monospace;
}

.pipeline-card:hover .step-num {
  color: rgba(200, 168, 102, 0.28);
  transition: color 0.3s;
}

h3 {
  font-size: 16px;
  font-weight: 900;
  margin: 0 0 12px;
  color: #ffffff;
}

.pipeline-card p {
  font-size: 13.5px;
  line-height: 1.65;
  color: var(--color-muted, #8e8e93);
  margin: 0;
}
</style>
