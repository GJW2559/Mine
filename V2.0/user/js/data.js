
async function fetchApiData() {
    const url = 'http://localhost:1890/API.txt';
    
    try {
        // 发起 GET 请求
        const response = await fetch(url, {
            method: 'GET',
            // 如果后端需要特定头信息，可在此添加
            // headers: {
            //     'Content-Type': 'text/plain'
            // }
        });

        // 检查响应状态码是否为 200-299
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // 将响应体解析为文本
        const data = await response.text();
        
        // 处理获取到的数据
        console.log('获取到的内容:', data);
        return data;

    } catch (error) {
        console.error('请求失败:', error);
    }
}

// 调用函数
fetchApiData();
var loadedText = "USername";