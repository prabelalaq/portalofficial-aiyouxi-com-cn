from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

SAMPLE_URL = "https://portalofficial-aiyouxi.com.cn"
SAMPLE_KEYWORD = "爱游戏"


@dataclass
class KeywordNote:
    """表示一条关键词笔记，包含标题、关键词、内容、关联链接和时间戳"""
    title: str
    keywords: List[str]
    content: str
    link: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)

    def formatted_output(self) -> str:
        lines = []
        lines.append("=" * 50)
        lines.append(f"标题：{self.title}")
        lines.append(f"关键词：{', '.join(self.keywords)}")
        lines.append(f"创建时间：{self.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
        if self.link:
            lines.append(f"关联链接：{self.link}")
        lines.append("-" * 50)
        lines.append(f"内容：")
        lines.append(self.content)
        lines.append("=" * 50)
        return "\n".join(lines)


@dataclass
class KeywordNoteCollection:
    """管理一系列 KeywordNote 对象，提供批量格式化输出"""
    notes: List[KeywordNote] = field(default_factory=list)

    def add_note(self, note: KeywordNote) -> None:
        self.notes.append(note)

    def format_all(self, separator: str = "\n---\n") -> str:
        return separator.join(note.formatted_output() for note in self.notes)

    def filter_by_keyword(self, keyword: str) -> List[KeywordNote]:
        return [
            note for note in self.notes
            if any(keyword.lower() in kw.lower() for kw in note.keywords)
        ]

    def summary(self) -> str:
        lines = []
        lines.append(f"笔记总数：{len(self.notes)}")
        if self.notes:
            lines.append(f"最早笔记：{self.notes[0].created_at.strftime('%Y-%m-%d')}")
            lines.append(f"最晚笔记：{self.notes[-1].created_at.strftime('%Y-%m-%d')}")
        return "\n".join(lines)


def demo_usage() -> None:
    collection = KeywordNoteCollection()

    note1 = KeywordNote(
        title="爱游戏平台介绍",
        keywords=[SAMPLE_KEYWORD, "平台", "游戏"],
        content="爱游戏是一个专注于提供优质游戏体验的官方平台，汇集了多种类型的游戏资源。",
        link=SAMPLE_URL,
    )

    note2 = KeywordNote(
        title="爱游戏特色功能",
        keywords=[SAMPLE_KEYWORD, "功能", "社区"],
        content="平台提供了丰富的社区互动功能，玩家可以分享攻略、组队开黑，并参与官方活动。",
        link=SAMPLE_URL,
    )

    note3 = KeywordNote(
        title="爱游戏最新动态",
        keywords=[SAMPLE_KEYWORD, "新闻", "更新"],
        content="爱游戏近期推出了全新版本，优化了界面和性能，并新增热门游戏专区。",
        link=SAMPLE_URL,
    )

    collection.add_note(note1)
    collection.add_note(note2)
    collection.add_note(note3)

    print("=== 全部笔记 ===")
    print(collection.format_all())

    print("\n=== 摘要 ===")
    print(collection.summary())

    print("\n=== 筛选含有「游戏」关键词的笔记 ===")
    matched = collection.filter_by_keyword("游戏")
    for note in matched:
        print(note.formatted_output())


if __name__ == "__main__":
    demo_usage()