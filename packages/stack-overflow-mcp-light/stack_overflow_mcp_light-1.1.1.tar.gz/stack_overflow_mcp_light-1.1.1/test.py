#!/usr/bin/env python3
"""Test script for Stack Overflow MCP tools."""

import asyncio
import json
import os
from typing import Any, Dict

# Set environment variables
os.environ["STACK_OVERFLOW_MCP_SHOW_LOGS"] = "true"

from stack_overflow_mcp_light.tools.questions import QuestionsClient
from stack_overflow_mcp_light.tools.answers import AnswersClient


def print_result(tool_name: str, result: Dict[str, Any]) -> None:
    """Print test results in a formatted way."""
    print(f"\n{'='*60}")
    print(f"🔧 TESTING: {tool_name}")
    print(f"{'='*60}")

    if "error" in result:
        print(f"❌ ERROR: {result['error']}")
    else:
        print("✅ SUCCESS")
        if "items" in result:
            items_count = len(result["items"])
            print(f"📊 Items returned: {items_count}")
            if items_count > 0:
                print(f"📋 Sample item keys: {list(result['items'][0].keys())}")
        else:
            print(f"📋 Result keys: {list(result.keys())}")

        # Print JSON for smaller results
        if len(json.dumps(result)) < 1000:
            print(f"📄 Full result:\n{json.dumps(result, indent=2)}")
        else:
            print("📄 Result too large to display (truncated)")


async def test_all_tools():
    """Test all MCP tools."""
    print("🚀 Starting Stack Overflow MCP Tools Test")
    print("=" * 60)

    # Initialize clients
    questions_client = QuestionsClient()
    answers_client = AnswersClient()

    # Test 1: get_top_answers (no parameters)
    print("\n🔧 1. Testing get_top_answers...")
    result_get_top_answers = await answers_client.get_top_answers(
        sort="votes", order="desc", page=1, page_size=5
    )
    print_result("get_top_answers", result_get_top_answers)
    # 11227809

    # Test 2: search_questions
    print("\n🔧 2. Testing search_questions...")
    result_search_questions = await questions_client.search_questions(
        q="python fastapi",
        page=1,
        page_size=3
    )
    print_result("search_questions", result_search_questions)

    # Test 3: fetch_question_answers (using a known question ID)
    print("\n🔧 3. Testing fetch_question_answers...")
    question_id = 11227809  # From top answers result
    result_fetch_question_answers = await questions_client.fetch_question_answers(
        question_id=question_id,
        include_body=True,
        include_answers=True
    )
    print_result("fetch_question_answers", result_fetch_question_answers)

    # Test 4: search_questions_by_tag
    print("\n🔧 4. Testing search_questions_by_tag...")
    result_search_questions_by_tag = await questions_client.search_questions_by_tag(
        tag="python",
        page=1,
        page_size=3
    )
    print_result("search_questions_by_tag", result_search_questions_by_tag)

    # Test 5: get_question_answers
    print("\n🔧 5. Testing get_question_answers...")
    result_get_question_answers = await questions_client.get_question_answers(
        question_id=question_id, page=1, page_size=5
    )
    print_result("get_question_answers", result_get_question_answers)


    # Test 6: get_answer_details (using an answer ID from previous results)
    print("\n🔧 6. Testing get_answer_details...")
    answer_id = 11227902  # From top answers result
    result_get_answer_details = await answers_client.get_answer_details(
        answer_id=answer_id,
        include_body=True,
        include_comments=True
    )
    print_result("get_answer_details", result_get_answer_details)

    print(f"\n{'='*60}")
    print("🎉 All tests completed!")
    print(f"{'='*60}")


if __name__ == "__main__":
    asyncio.run(test_all_tools())