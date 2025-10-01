"""적응형 그리드 시스템"""

from typing import Dict, Tuple
from dataclasses import dataclass

from ..utils.logger import get_logger


@dataclass
class GridConfig:
    """그리드 설정"""
    max_columns: int = 12
    min_column_width: int = 160
    gap: int = 16
    padding: int = 32


class AdaptiveGridManager:
    """적응형 그리드 매니저"""
    
    def __init__(self, config: GridConfig = None):
        self.config = config or GridConfig()
        self.logger = get_logger("AdaptiveGridManager")
        
        # 컴포넌트 배치 추적
        self.placed_components: Dict[str, Tuple[int, int, int, int]] = {}
        self.occupied_cells: set[Tuple[int, int]] = set()
        
        # 자동 배치 커서
        self.next_row = 0
        self.next_col = 0
        
    def add_component(self, 
                     component_id: str, 
                     width: int = 2, 
                     height: int = 2,
                     row: int = None, 
                     col: int = None) -> Tuple[int, int, int, int]:
        """컴포넌트 추가"""
        
        # 수동 배치 또는 자동 배치
        if row is not None and col is not None:
            if self._is_position_available(row, col, width, height):
                final_row, final_col = row, col
            else:
                self.logger.info(f"⚠️ 위치 충돌 ({row}, {col}) - 자동 배치로 변경")
                final_row, final_col = self._find_auto_position(width, height)
        else:
            final_row, final_col = self._find_auto_position(width, height)
        
        # 배치 등록
        self.placed_components[component_id] = (final_row, final_col, width, height)
        self._occupy_cells(final_row, final_col, width, height)
        
        self.logger.info(f"✅ 컴포넌트 배치: {component_id} at ({final_row}, {final_col}) {width}×{height}")
        return final_row, final_col, width, height
    
    def _find_auto_position(self, width: int, height: int) -> Tuple[int, int]:
        """자동 배치 위치 찾기"""
        
        # 현재 행에서 배치 시도
        for try_col in range(self.next_col, self.config.max_columns - width + 1):
            if self._is_position_available(self.next_row, try_col, width, height):
                row, col = self.next_row, try_col
                
                # 다음 위치 업데이트
                self.next_col = col + width
                if self.next_col >= self.config.max_columns:
                    self.next_row += height
                    self.next_col = 0
                
                return row, col
        
        # 다음 행들에서 검색
        return self._find_next_row(width, height)
    
    def _find_next_row(self, width: int, height: int) -> Tuple[int, int]:
        """다음 사용 가능한 행 찾기"""
        search_row = self.next_row
        
        for _ in range(50):  # 최대 50행 검색
            search_row += 1
            
            # 0열부터 시도
            if self._is_position_available(search_row, 0, width, height):
                self.next_row = search_row
                self.next_col = width
                if self.next_col >= self.config.max_columns:
                    self.next_row += height
                    self.next_col = 0
                return search_row, 0
            
            # 다른 열들 시도
            for try_col in range(1, self.config.max_columns - width + 1):
                if self._is_position_available(search_row, try_col, width, height):
                    self.next_row = search_row
                    self.next_col = try_col + width
                    if self.next_col >= self.config.max_columns:
                        self.next_row += height
                        self.next_col = 0
                    return search_row, try_col
        
        # 안전장치
        self.next_row = search_row
        self.next_col = 0
        return search_row, 0
    
    def _is_position_available(self, row: int, col: int, width: int, height: int) -> bool:
        """위치 사용 가능 여부 확인"""
        for r in range(row, row + height):
            for c in range(col, min(col + width, self.config.max_columns)):
                if (r, c) in self.occupied_cells:
                    return False
        return True
    
    def _occupy_cells(self, row: int, col: int, width: int, height: int):
        """셀 점유 표시"""
        for r in range(row, row + height):
            for c in range(col, min(col + width, self.config.max_columns)):
                self.occupied_cells.add((r, c))
    
    def get_component_classes(self, component_id: str, screen_width: int = 1920) -> str:
        """컴포넌트 CSS 클래스 생성
        
        기본 screen_width를 1920으로 설정하여 초기 렌더링 시 
        대부분의 컴포넌트가 한 행에 배치되도록 함 (JavaScript 업데이트 전까지)
        """
        if component_id not in self.placed_components:
            return "grid-item"
        
        current_columns = self.calculate_current_columns(screen_width)
        
        # 적응형 레이아웃 계산 사용
        adaptive_layout = self.calculate_adaptive_layout(current_columns)
        
        if component_id in adaptive_layout:
            row, col, width, height = adaptive_layout[component_id]
        else:
            # 폴백: 기존 위치 사용
            row, col, width, height = self.placed_components[component_id]
            width = min(width, current_columns)  # 최소한의 조정
        
        classes = [
            "grid-item",
            f"col-start-{col + 1}",
            f"col-span-{width}",
            f"row-start-{row + 1}",
            f"row-span-{height}"
        ]
        
        return " ".join(classes)
    
    def calculate_adaptive_layout(self, current_columns: int) -> Dict[str, Tuple[int, int, int, int]]:
        """컬럼 수 변경 시 전체 레이아웃 재계산"""
        new_layout = {}
        occupied = set()
        current_row = 0
        current_col = 0
        
        # 컴포넌트들을 원래 배치 순서대로 정렬 (row, col 기준)
        sorted_components = sorted(
            self.placed_components.items(),
            key=lambda x: (x[1][0], x[1][1])  # (row, col) 순서
        )
        
        for comp_id, (orig_row, orig_col, orig_width, orig_height) in sorted_components:
            # 현재 컬럼 수에 맞게 너비 조정
            adaptive_width = min(orig_width, current_columns)
            
            # 현재 행에서 배치 가능한지 확인
            if current_col + adaptive_width > current_columns:
                # 다음 행으로 래핑
                current_row += 1
                current_col = 0
            
            # 충돌 검사 및 안전한 위치 찾기
            final_row, final_col = self._find_safe_position(
                occupied, current_row, current_col, adaptive_width, orig_height, current_columns
            )
            
            # 새 레이아웃에 등록
            new_layout[comp_id] = (final_row, final_col, adaptive_width, orig_height)
            
            # 점유 영역 마킹
            for r in range(final_row, final_row + orig_height):
                for c in range(final_col, final_col + adaptive_width):
                    occupied.add((r, c))
            
            # 다음 위치 업데이트
            current_col = final_col + adaptive_width
            current_row = final_row
        
        return new_layout
    
    def _find_safe_position(self, occupied: set, preferred_row: int, preferred_col: int,
                           width: int, height: int, max_columns: int) -> Tuple[int, int]:
        """충돌하지 않는 안전한 위치 찾기"""
        
        # 선호 위치에서 배치 가능한지 먼저 확인
        if self._is_adaptive_position_available(occupied, preferred_row, preferred_col, width, height, max_columns):
            return preferred_row, preferred_col
        
        # 같은 행의 다른 위치 시도
        for try_col in range(0, max_columns - width + 1):
            if self._is_adaptive_position_available(occupied, preferred_row, try_col, width, height, max_columns):
                return preferred_row, try_col
        
        # 다음 행들에서 검색
        for try_row in range(preferred_row + 1, preferred_row + 20):  # 최대 20행 검색
            for try_col in range(0, max_columns - width + 1):
                if self._is_adaptive_position_available(occupied, try_row, try_col, width, height, max_columns):
                    return try_row, try_col
        
        # 안전장치: 강제 배치
        return preferred_row + 1, 0
    
    def _is_adaptive_position_available(self, occupied: set, row: int, col: int,
                                       width: int, height: int, max_columns: int) -> bool:
        """적응형 레이아웃에서 위치 사용 가능 여부 확인"""
        # 경계 검사
        if col + width > max_columns or row < 0 or col < 0:
            return False
        
        # 점유 셀 검사
        for r in range(row, row + height):
            for c in range(col, col + width):
                if (r, c) in occupied:
                    return False
        
        return True

    def calculate_current_columns(self, screen_width: int) -> int:
        """화면 너비에 따른 현재 컬럼 수 계산"""
        available_width = screen_width - (self.config.padding * 2)
        theoretical_columns = (available_width + self.config.gap) // (self.config.min_column_width + self.config.gap)
        current_columns = min(theoretical_columns, self.config.max_columns)
        current_columns = max(current_columns, 1)
        
        return int(current_columns)
    
    def get_css_styles(self) -> str:
        """적응형 CSS 스타일 생성"""
        return f"""
.adaptive-grid-container {{
    display: grid;
    width: 100%;
    min-height: 100vh;
    padding: {self.config.padding}px;
    gap: {self.config.gap}px;
    box-sizing: border-box;
    
    /* 기본 12컬럼 그리드 */
    grid-template-columns: repeat(12, 1fr);
    /* 행 높이 고정: 정확한 비율을 위해 고정 높이 사용 */
    grid-template-rows: repeat(20, 180px); /* 모든 행을 180px 고정 */
    /* 추가 행이 필요한 경우를 위한 암시적 행 설정 */
    grid-auto-rows: 180px;
    
    /* 부드러운 전환 */
    transition: grid-template-columns 0.3s ease;
}}

/* 적응형 컬럼 조정 */
.adaptive-grid-container.cols-1 {{ grid-template-columns: repeat(1, 1fr); }}
.adaptive-grid-container.cols-2 {{ grid-template-columns: repeat(2, 1fr); }}
.adaptive-grid-container.cols-3 {{ grid-template-columns: repeat(3, 1fr); }}
.adaptive-grid-container.cols-4 {{ grid-template-columns: repeat(4, 1fr); }}
.adaptive-grid-container.cols-5 {{ grid-template-columns: repeat(5, 1fr); }}
.adaptive-grid-container.cols-6 {{ grid-template-columns: repeat(6, 1fr); }}
.adaptive-grid-container.cols-7 {{ grid-template-columns: repeat(7, 1fr); }}
.adaptive-grid-container.cols-8 {{ grid-template-columns: repeat(8, 1fr); }}
.adaptive-grid-container.cols-9 {{ grid-template-columns: repeat(9, 1fr); }}
.adaptive-grid-container.cols-10 {{ grid-template-columns: repeat(10, 1fr); }}
.adaptive-grid-container.cols-11 {{ grid-template-columns: repeat(11, 1fr); }}
.adaptive-grid-container.cols-12 {{ grid-template-columns: repeat(12, 1fr); }}

/* 그리드 아이템 */
.grid-item {{
    display: flex;
    flex-direction: column;
    min-height: 100px;
    transition: all 0.3s ease;
}}

/* 카드 스타일 */
.grid-item .q-card {{
    height: 100%;
    border-radius: 8px;
    border: 1px solid #e0e0e0;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    background: white;
    padding: 0;
    display: flex;
    flex-direction: column;
}}

.grid-item .q-card:hover {{
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    transform: translateY(-2px);
}}

/* 반응형 조정 */
@media (max-width: 480px) {{
    .adaptive-grid-container {{
        padding: 16px;
        gap: 8px;
    }}
    .grid-item .q-card {{
        padding: 0.5rem;
    }}
}}
"""
    
    def get_javascript_utilities(self) -> str:
        """JavaScript 유틸리티"""
        return f"""
class AdaptiveGrid {{
    constructor(minColumnWidth = {self.config.min_column_width}) {{
        this.minColumnWidth = minColumnWidth;
        this.gap = {self.config.gap};
        this.padding = {self.config.padding};
        this.maxColumns = 12;
        this.currentColumns = 12;
        this.container = null;
        this.components = new Map(); // 컴포넌트 정보 저장
        
        this.init();
    }}
    
    init() {{
        this.container = document.querySelector('.adaptive-grid-container');
        if (!this.container) return;
        
        // 기존 컴포넌트 정보 수집
        this.collectComponentInfo();
        
        // 초기 그리드 업데이트 (서버 렌더링과 클라이언트 동기화)
        this.updateGrid();
        
        // 초기 행 템플릿 설정
        this.updateGridRowTemplate();
        
        // 초기 로딩 완료 후 즉시 한 번 더 업데이트 (타이밍 이슈 해결)
        setTimeout(() => {{
            this.updateGrid();
        }}, 50);
        
        window.addEventListener('resize', () => this.updateGrid());
    }}
    
    collectComponentInfo() {{
        // 그리드 아이템들의 원본 정보 수집
        const items = this.container.querySelectorAll('.grid-item');
        
        // 기존 정보 초기화 (재수집 시를 위해)
        this.components.clear();
        
        items.forEach((item, index) => {{
            const classes = item.className;
            const colStartMatch = classes.match(/col-start-(\\d+)/);
            const colSpanMatch = classes.match(/col-span-(\\d+)/);
            const rowStartMatch = classes.match(/row-start-(\\d+)/);
            const rowSpanMatch = classes.match(/row-span-(\\d+)/);
            
            if (colStartMatch && colSpanMatch && rowStartMatch && rowSpanMatch) {{
                const id = item.id || `item-${{index}}`;
                this.components.set(id, {{
                    element: item,
                    originalCol: parseInt(colStartMatch[1]) - 1,
                    originalWidth: parseInt(colSpanMatch[1]),
                    originalRow: parseInt(rowStartMatch[1]) - 1,
                    originalHeight: parseInt(rowSpanMatch[1]),
                    originalOrder: index  // 배치 순서 유지
                }});
                item.id = id; // ID 설정
            }}
        }});
    }}
    
    calculateColumns(screenWidth = window.innerWidth) {{
        const availableWidth = screenWidth - (this.padding * 2);
        const theoreticalColumns = Math.floor((availableWidth + this.gap) / (this.minColumnWidth + this.gap));
        return Math.max(1, Math.min(theoreticalColumns, this.maxColumns));
    }}
    
    // 적응형 레이아웃 재계산
    calculateAdaptiveLayout(currentColumns) {{
        const newLayout = new Map();
        const occupied = new Set();
        let currentRow = 0;
        let currentCol = 0;
        
        // 원래 배치 순서대로 정렬 (row, col 순서)
        const sortedComponents = Array.from(this.components.entries()).sort((a, b) => {{
            const [, aInfo] = a;
            const [, bInfo] = b;
            if (aInfo.originalRow !== bInfo.originalRow) {{
                return aInfo.originalRow - bInfo.originalRow;
            }}
            return aInfo.originalCol - bInfo.originalCol;
        }});
        
        for (const [compId, info] of sortedComponents) {{
            const {{ originalWidth, originalHeight }} = info;
            
            // 현재 컬럼 수에 맞게 너비 조정
            const adaptiveWidth = Math.min(originalWidth, currentColumns);
            
            // 현재 행에서 배치 가능한지 확인
            if (currentCol + adaptiveWidth > currentColumns) {{
                // 다음 행으로 래핑
                currentRow++;
                currentCol = 0;
            }}
            
            // 충돌 검사 및 안전한 위치 찾기
            const [finalRow, finalCol] = this.findSafePosition(
                occupied, currentRow, currentCol, adaptiveWidth, originalHeight, currentColumns
            );
            
            newLayout.set(compId, {{
                row: finalRow,
                col: finalCol,
                width: adaptiveWidth,
                height: originalHeight
            }});
            
            // 점유 영역 마킹
            for (let r = finalRow; r < finalRow + originalHeight; r++) {{
                for (let c = finalCol; c < finalCol + adaptiveWidth; c++) {{
                    occupied.add(`${{r}}-${{c}}`);
                }}
            }}
            
            // 다음 위치 업데이트
            currentCol = finalCol + adaptiveWidth;
            currentRow = finalRow;
        }}
        
        return newLayout;
    }}
    
    findSafePosition(occupied, preferredRow, preferredCol, width, height, maxColumns) {{
        // 선호 위치 확인
        if (this.isPositionAvailable(occupied, preferredRow, preferredCol, width, height, maxColumns)) {{
            return [preferredRow, preferredCol];
        }}
        
        // 같은 행의 다른 위치 시도
        for (let col = 0; col <= maxColumns - width; col++) {{
            if (this.isPositionAvailable(occupied, preferredRow, col, width, height, maxColumns)) {{
                return [preferredRow, col];
            }}
        }}
        
        // 다음 행들에서 검색
        for (let row = preferredRow + 1; row < preferredRow + 20; row++) {{
            for (let col = 0; col <= maxColumns - width; col++) {{
                if (this.isPositionAvailable(occupied, row, col, width, height, maxColumns)) {{
                    return [row, col];
                }}
            }}
        }}
        
        // 안전장치
        return [preferredRow + 1, 0];
    }}
    
    isPositionAvailable(occupied, row, col, width, height, maxColumns) {{
        if (col + width > maxColumns || row < 0 || col < 0) {{
            return false;
        }}
        
        for (let r = row; r < row + height; r++) {{
            for (let c = col; c < col + width; c++) {{
                if (occupied.has(`${{r}}-${{c}}`)) {{
                    return false;
                }}
            }}
        }}
        
        return true;
    }}
    
    updateGrid() {{
        if (!this.container) return;
        
        const newColumns = this.calculateColumns();
        
        if (newColumns !== this.currentColumns) {{
            this.container.classList.remove(`cols-${{this.currentColumns}}`);
            this.container.classList.add(`cols-${{newColumns}}`);
            
            this.currentColumns = newColumns;
            
            // 핵심: 적응형 레이아웃 재계산 및 적용
            this.updateComponentLayout(newColumns);
            
            // 행 높이 통일: 필요한 행 수 계산 및 템플릿 업데이트
            this.updateGridRowTemplate();
            
            // 커스텀 이벤트 발생
            window.dispatchEvent(new CustomEvent('gridColumnsChanged', {{
                detail: {{ columns: newColumns, screenWidth: window.innerWidth }}
            }}));
        }} else {{
            // 컬럼 수는 같지만 레이아웃을 강제로 한 번 더 업데이트 (초기화 타이밍 이슈 해결)
            this.updateComponentLayout(newColumns);
        }}
    }}
    
    updateComponentLayout(currentColumns) {{
        // 적응형 레이아웃 계산
        const newLayout = this.calculateAdaptiveLayout(currentColumns);
        
        // 각 컴포넌트 위치 업데이트
        this.components.forEach((info, id) => {{
            const {{ element }} = info;
            const newPosition = newLayout.get(id);
            
            if (newPosition) {{
                // 기존 클래스 제거
                element.className = element.className.replace(/col-start-\\d+|col-span-\\d+|row-start-\\d+/g, '').trim();
                
                // 새로운 클래스 추가
                element.classList.add(`col-start-${{newPosition.col + 1}}`);
                element.classList.add(`col-span-${{newPosition.width}}`);
                element.classList.add(`row-start-${{newPosition.row + 1}}`);
            }}
        }});
        
        // 컴포넌트 업데이트 후 행 템플릿도 업데이트
        setTimeout(() => this.updateGridRowTemplate(), 100); // 짧은 지연 후 업데이트
    }}
    
    // 행 높이 통일을 위한 동적 행 템플릿 업데이트
    updateGridRowTemplate() {{
        if (!this.container) return;
        
        // 현재 레이아웃에서 최대 행 수 계산
        const currentLayout = this.calculateAdaptiveLayout(this.currentColumns);
        let maxRow = 0;
        
        currentLayout.forEach(position => {{
            const endRow = position.row + position.height;
            maxRow = Math.max(maxRow, endRow);
        }});
        
        // 여유 행 추가 (최소 5행 여유)
        const totalRows = Math.max(maxRow + 5, 10);
        
        // CSS 그리드 템플릿 고정 높이로 업데이트 (정확한 비율을 위해)
        this.container.style.gridTemplateRows = `repeat(${{totalRows}}, 180px)`;
    }}
    
    getInfo() {{
        return {{
            currentColumns: this.currentColumns,
            screenWidth: window.innerWidth,
            minColumnWidth: this.minColumnWidth,
            components: this.components.size,
            adaptiveLayout: this.calculateAdaptiveLayout(this.currentColumns)
        }};
    }}
}}

// 자동 초기화 - 더 안정적인 타이밍
document.addEventListener('DOMContentLoaded', () => {{
    window.adaptiveGrid = new AdaptiveGrid();
}});

// 🔧 추가 안전장치: 모든 리소스 로딩 완료 후에도 한 번 더 확인
window.addEventListener('load', () => {{
    if (window.adaptiveGrid) {{
        setTimeout(() => {{
            window.adaptiveGrid.updateGrid();
        }}, 100);
    }}
}});

// 콘솔 명령어
window.getGridInfo = () => {{
    if (window.adaptiveGrid) {{
        const info = window.adaptiveGrid.getInfo();
        console.table(info);
    }}
}};

// 디버그 명령어
window.testLayout = (columns) => {{
    if (window.adaptiveGrid) {{
        const layout = window.adaptiveGrid.calculateAdaptiveLayout(columns);
        console.table(Array.from(layout.entries()));
    }}
}};
"""
    
    def get_stats(self) -> Dict:
        """현재 그리드 통계"""
        return {
            'total_components': len(self.placed_components),
            'occupied_cells': len(self.occupied_cells),
            'next_position': (self.next_row, self.next_col),
            'config': {
                'max_columns': self.config.max_columns,
                'min_column_width': self.config.min_column_width,
                'gap': self.config.gap,
                'padding': self.config.padding
            }
        }