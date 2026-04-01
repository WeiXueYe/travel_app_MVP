// API连接测试脚本
async function testAPI() {
    try {
        console.log('🔍 开始测试API连接...');

        // 测试基础API调用
        const response = await fetch('http://localhost:8000/api/v1/travels');
        const data = await response.json();

        console.log('✅ API连接成功！');
        console.log('📊 返回数据:', data);

        if (data.length > 0) {
            console.log('🎉 第一个旅行内容:');
            console.log('   - 标题:', data[0].title);
            console.log('   - slug:', data[0].slug);
            console.log('   - 体验类型:', data[0].experience_type);
            console.log('   - 视觉风格:', data[0].visual_style);
            console.log('   - 情感基调:', data[0].emotional_tone);
        }

        return true;
    } catch (error) {
        console.error('❌ API连接失败:', error.message);
        return false;
    }
}

// 运行测试
testAPI();