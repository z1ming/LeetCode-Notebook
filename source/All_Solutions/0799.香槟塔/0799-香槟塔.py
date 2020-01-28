class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        flow_in = [[poured]]
        flag = True
        
        while flag and len(flow_in)<min(100, query_row+1):
            flow_in.append([0.0 for _ in range(len(flow_in[-1])+1)])
            flag = False
            for i, flow in enumerate(flow_in[-2]):
                if flow>1:
                    over_flow = (flow-1)/2
                    flow_in[-1][i] += over_flow
                    flow_in[-1][i+1] += over_flow
                    flag = True
        
        if query_row>len(flow_in)-1:
            return 0.0
        else:
            return min(1, flow_in[query_row][query_glass])