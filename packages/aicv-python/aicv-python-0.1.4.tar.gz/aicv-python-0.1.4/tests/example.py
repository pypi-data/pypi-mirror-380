#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AiCV Python SDK 使用示例
展示如何使用AiCV SDK进行简历分析
"""

import os
from typing import Optional
from aicv import AiCVClient


def analyze_resume_example():
    """简历分析示例"""
    
    # 1. 获取API密钥（从环境变量或直接设置）
    api_key = os.getenv('AICV_API_KEY', 'string')
    
    # 2. 示例简历内容
    resume_text = """
    张三
    软件工程师

    联系方式：
    - 邮箱：zhangsan@example.com
    - 电话：138-0000-0000
    - 地址：北京市朝阳区

    工作经验：
    2021-2023  ABC科技有限公司  软件工程师
    - 负责后端API开发和维护
    - 使用Python和FastAPI框架
    - 参与数据库设计和优化
    - 协助前端团队进行接口对接

    技能：
    - 编程语言：Python, JavaScript, SQL
    - 框架：FastAPI, Django, React
    - 数据库：MySQL, PostgreSQL, Redis
    - 工具：Git, Docker, Linux

    教育背景：
    2017-2021  北京理工大学  计算机科学与技术  学士学位

    项目经验：
    1. 电商平台后端开发
       - 使用FastAPI构建RESTful API
       - 实现用户认证和权限管理
       - 优化数据库查询性能

    2. 微服务架构设计
       - 使用Docker容器化部署
       - 实现服务间通信和负载均衡
       - 监控和日志系统集成
    """
    
    # 3. 目标职位信息
    job_title = "高级软件工程师"
    job_description = "负责大型分布式系统的设计和开发，要求具备微服务架构经验"
    
    print("🎯 AiCV 简历分析示例")
    print("=" * 50)
    print(f"📝 分析职位: {job_title}")
    print(f"📋 职位描述: {job_description}")
    print()
    
    try:
        # 4. 创建客户端并分析简历
        print("🔍 正在连接AiCV服务...")
        with AiCVClient(api_key=api_key, verify=False) as client:
            print("✅ 连接成功！")
            print("📊 正在分析简历...")
            
            # 获取简历建议
            suggestions = client.get_resume_suggestions(
                resume_text=resume_text,
                job_title=job_title,
                job_description=job_description
            )
            
            if suggestions:
                print("✅ 分析完成！")
                print("📈 改进建议:")
                print("-" * 30)
                
                # 显示建议
                if isinstance(suggestions, list):
                    for i, suggestion in enumerate(suggestions, 1):
                        print(f"{i}. {suggestion}")
                elif isinstance(suggestions, dict):
                    # 处理结构化数据
                    if 'data' in suggestions and 'improvements' in suggestions['data']:
                        improvements = suggestions['data']['improvements']
                        for i, item in enumerate(improvements, 1):
                            print(f"{i}. {item.get('problem', '')}")
                            print(f"   💡 {item.get('suggestion', '')}")
                            print()
                    else:
                        print("📄 返回数据:", suggestions)
                else:
                    print("📄 建议内容:", suggestions)
            else:
                print("⚠️  未获得建议，请检查简历内容")
                
    except Exception as e:
        print(f"❌ 分析失败: {str(e)}")
        print("💡 请检查:")
        print("   - API密钥是否正确")
        print("   - 网络连接是否正常")
        print("   - 服务是否可用")


def cloud_deployment_example():
    """云端部署异步回调示例"""
    
    print("\n☁️ 云端部署异步回调示例")
    print("=" * 40)
    
    api_key = os.getenv('AICV_API_KEY', 'your-api-key')
    
    # 云端部署配置
    client = AiCVClient(
        api_key=api_key,
        base_url="https://api.aicv.chat",
        timeout=600.0,
        verify=True  # 生产环境启用SSL验证
    )
    
    try:
        print("🚀 提交异步分析任务...")
        
        # 使用异步回调
        result = client.get_resume_suggestions(
            resume_text="云端部署测试简历内容...",
            job_title="云端架构师",
            job_description="负责云端服务架构设计...",
            callback_url="https://your-domain.com/webhook/aicv-callback"
        )
        
        print("✅ 任务已提交！")
        print(f"📋 任务ID: {result.get('task_id', 'N/A')}")
        print("🔄 结果将通过回调地址返回")
        print("💡 回调地址: https://your-domain.com/webhook/aicv-callback")
        
    except Exception as e:
        print(f"❌ 异步任务提交失败: {e}")


def development_environment_example():
    """开发环境配置示例"""
    
    print("\n🛠️ 开发环境配置示例")
    print("=" * 35)
    
    api_key = os.getenv('AICV_API_KEY', 'dev-test-key')
    
    # 开发环境配置
    client = AiCVClient(
        api_key=api_key,
        verify=False,  # 开发环境禁用SSL验证
        timeout=30.0,  # 开发环境使用较短超时时间
        base_url="https://api.aicv.chat"
    )
    
    try:
        print("🔧 开发环境测试...")
        with client as c:
            result = c.get_resume_suggestions(
                resume_text="开发环境测试简历",
                job_title="开发测试职位",
                job_description="开发环境测试描述"
            )
            print("✅ 开发环境测试成功！")
            print(f"📊 测试结果: {result}")
            
    except Exception as e:
        print(f"❌ 开发环境测试失败: {e}")
        print("💡 开发环境提示:")
        print("   - verify=False 禁用SSL验证")
        print("   - 较短的timeout时间")
        print("   - 使用测试API密钥")


def basic_usage_example():
    """基本使用示例"""
    
    print("\n🚀 基本使用示例")
    print("=" * 30)
    
    # 示例1: 基本连接测试
    print("1. 基本连接测试:")
    try:
        client = AiCVClient(api_key="test-key")
        print("   ✅ 客户端创建成功")
    except Exception as e:
        print(f"   ❌ 客户端创建失败: {e}")
    
    # 示例2: 上下文管理器使用
    print("\n2. 上下文管理器使用:")
    try:
        with AiCVClient(api_key="test-key") as client:
            print("   ✅ 上下文管理器工作正常")
    except Exception as e:
        print(f"   ❌ 上下文管理器失败: {e}")
    
    # 示例3: 错误处理
    print("\n3. 错误处理示例:")
    try:
        client = AiCVClient(api_key="invalid-key")
        # 这里会触发API调用，演示错误处理
        suggestions = client.get_resume_suggestions("test resume")
    except Exception as e:
        print(f"   ✅ 错误处理正常: {type(e).__name__}")


def main():
    """主函数"""
    print("🎉 AiCV Python SDK 使用示例")
    print("=" * 60)
    
    # 显示SDK信息
    try:
        import aicv
        print(f"📦 SDK版本: {getattr(aicv, '__version__', '未知')}")
        print(f"📁 模块路径: {aicv.__file__}")
    except ImportError:
        print("❌ 无法导入AiCV SDK，请先安装: pip install aicv")
        return
    
    print()
    
    # 基本使用示例
    basic_usage_example()
    
    # 简历分析示例
    analyze_resume_example()
    
    # 云端部署异步回调示例
    cloud_deployment_example()
    
    # 开发环境配置示例
    development_environment_example()
    
    print("\n💡 使用提示:")
    print("1. 获取API密钥: https://aicv.chat")
    print("2. 设置环境变量: export AICV_API_KEY=your-key")
    print("3. 使用上下文管理器管理连接")
    print("4. 正确处理异常情况")
    print("5. 根据返回结果优化简历内容")
    print("6. 云端部署使用异步回调机制")
    print("7. 开发环境设置verify=False禁用SSL验证")
    
    print("\n🎯 示例完成！")


if __name__ == '__main__':
    main()
