from mapFolding.dataBaskets import Array1DElephino, Array1DLeavesTotal, Array3DLeavesTotal, DatatypeElephino, DatatypeFoldsTotal, DatatypeLeavesTotal, MapFoldingState
from numba import jit

@jit(cache=True, error_model='numpy', fastmath=True, forceinline=True)
def count(groupsOfFolds: DatatypeFoldsTotal, gap1ndex: DatatypeElephino, gap1ndexCeiling: DatatypeElephino, indexDimension: DatatypeLeavesTotal, indexLeaf: DatatypeLeavesTotal, indexMiniGap: DatatypeElephino, leaf1ndex: DatatypeLeavesTotal, leafConnectee: DatatypeLeavesTotal, dimensionsUnconstrained: DatatypeLeavesTotal, countDimensionsGapped: Array1DLeavesTotal, gapRangeStart: Array1DElephino, gapsWhere: Array1DLeavesTotal, leafAbove: Array1DLeavesTotal, leafBelow: Array1DLeavesTotal, leafComparison: Array1DLeavesTotal, connectionGraph: Array3DLeavesTotal, dimensionsTotal: DatatypeLeavesTotal, leavesTotal: DatatypeLeavesTotal) -> tuple[DatatypeFoldsTotal, DatatypeElephino, DatatypeElephino, DatatypeLeavesTotal, DatatypeLeavesTotal, DatatypeElephino, DatatypeLeavesTotal, DatatypeLeavesTotal, DatatypeLeavesTotal, Array1DLeavesTotal, Array1DElephino, Array1DLeavesTotal, Array1DLeavesTotal, Array1DLeavesTotal, Array1DLeavesTotal, Array3DLeavesTotal, DatatypeLeavesTotal, DatatypeLeavesTotal]:
    while leaf1ndex > 0:
        if leaf1ndex <= 1 or leafBelow[0] == 1:
            if leaf1ndex > leavesTotal:
                indexLeaf = 0
                leafConnectee = 0
                while leafConnectee < leavesTotal + 1:
                    leafNumber = int(leafBelow[indexLeaf])
                    leafComparison[leafConnectee] = (leafNumber - indexLeaf + leavesTotal) % leavesTotal
                    indexLeaf = leafNumber
                    leafConnectee += 1
                indexInMiddle = leavesTotal // 2
                indexMiniGap = 0
                while indexMiniGap < leavesTotal + 1:
                    ImaSymmetricFold = True
                    leafConnectee = 0
                    while leafConnectee < indexInMiddle:
                        if leafComparison[(indexMiniGap + leafConnectee) % (leavesTotal + 1)] != leafComparison[(indexMiniGap + leavesTotal - 1 - leafConnectee) % (leavesTotal + 1)]:
                            ImaSymmetricFold = False
                            break
                        leafConnectee += 1
                    groupsOfFolds += ImaSymmetricFold
                    indexMiniGap += 1
            else:
                dimensionsUnconstrained = dimensionsTotal
                gap1ndexCeiling = gapRangeStart[leaf1ndex - 1]
                indexDimension = 0
                while indexDimension < dimensionsTotal:
                    leafConnectee = connectionGraph[indexDimension, leaf1ndex, leaf1ndex]
                    if leafConnectee == leaf1ndex:
                        dimensionsUnconstrained -= 1
                    else:
                        while leafConnectee != leaf1ndex:
                            gapsWhere[gap1ndexCeiling] = leafConnectee
                            if countDimensionsGapped[leafConnectee] == 0:
                                gap1ndexCeiling += 1
                            countDimensionsGapped[leafConnectee] += 1
                            leafConnectee = connectionGraph[indexDimension, leaf1ndex, leafBelow[leafConnectee]]
                    indexDimension += 1
                if not dimensionsUnconstrained:
                    indexLeaf = 0
                    while indexLeaf < leaf1ndex:
                        gapsWhere[gap1ndexCeiling] = indexLeaf
                        gap1ndexCeiling += 1
                        indexLeaf += 1
                indexMiniGap = gap1ndex
                while indexMiniGap < gap1ndexCeiling:
                    gapsWhere[gap1ndex] = gapsWhere[indexMiniGap]
                    if countDimensionsGapped[gapsWhere[indexMiniGap]] == dimensionsUnconstrained:
                        gap1ndex += 1
                    countDimensionsGapped[gapsWhere[indexMiniGap]] = 0
                    indexMiniGap += 1
        while leaf1ndex > 0 and gap1ndex == gapRangeStart[leaf1ndex - 1]:
            leaf1ndex -= 1
            leafBelow[leafAbove[leaf1ndex]] = leafBelow[leaf1ndex]
            leafAbove[leafBelow[leaf1ndex]] = leafAbove[leaf1ndex]
        if leaf1ndex > 0:
            gap1ndex -= 1
            leafAbove[leaf1ndex] = gapsWhere[gap1ndex]
            leafBelow[leaf1ndex] = leafBelow[leafAbove[leaf1ndex]]
            leafBelow[leafAbove[leaf1ndex]] = leaf1ndex
            leafAbove[leafBelow[leaf1ndex]] = leaf1ndex
            gapRangeStart[leaf1ndex] = gap1ndex
            leaf1ndex += 1
    groupsOfFolds = (groupsOfFolds + 1) // 2
    return (groupsOfFolds, gap1ndex, gap1ndexCeiling, indexDimension, indexLeaf, indexMiniGap, leaf1ndex, leafConnectee, dimensionsUnconstrained, countDimensionsGapped, gapRangeStart, gapsWhere, leafAbove, leafBelow, leafComparison, connectionGraph, dimensionsTotal, leavesTotal)

def doTheNeedful(state: MapFoldingState) -> MapFoldingState:
    mapShape: tuple[DatatypeLeavesTotal, ...] = state.mapShape
    groupsOfFolds: DatatypeFoldsTotal = state.groupsOfFolds
    gap1ndex: DatatypeElephino = state.gap1ndex
    gap1ndexCeiling: DatatypeElephino = state.gap1ndexCeiling
    indexDimension: DatatypeLeavesTotal = state.indexDimension
    indexLeaf: DatatypeLeavesTotal = state.indexLeaf
    indexMiniGap: DatatypeElephino = state.indexMiniGap
    leaf1ndex: DatatypeLeavesTotal = state.leaf1ndex
    leafConnectee: DatatypeLeavesTotal = state.leafConnectee
    dimensionsUnconstrained: DatatypeLeavesTotal = state.dimensionsUnconstrained
    countDimensionsGapped: Array1DLeavesTotal = state.countDimensionsGapped
    gapRangeStart: Array1DElephino = state.gapRangeStart
    gapsWhere: Array1DLeavesTotal = state.gapsWhere
    leafAbove: Array1DLeavesTotal = state.leafAbove
    leafBelow: Array1DLeavesTotal = state.leafBelow
    leafComparison: Array1DLeavesTotal = state.leafComparison
    connectionGraph: Array3DLeavesTotal = state.connectionGraph
    dimensionsTotal: DatatypeLeavesTotal = state.dimensionsTotal
    leavesTotal: DatatypeLeavesTotal = state.leavesTotal
    groupsOfFolds, gap1ndex, gap1ndexCeiling, indexDimension, indexLeaf, indexMiniGap, leaf1ndex, leafConnectee, dimensionsUnconstrained, countDimensionsGapped, gapRangeStart, gapsWhere, leafAbove, leafBelow, leafComparison, connectionGraph, dimensionsTotal, leavesTotal = count(groupsOfFolds, gap1ndex, gap1ndexCeiling, indexDimension, indexLeaf, indexMiniGap, leaf1ndex, leafConnectee, dimensionsUnconstrained, countDimensionsGapped, gapRangeStart, gapsWhere, leafAbove, leafBelow, leafComparison, connectionGraph, dimensionsTotal, leavesTotal)
    state = MapFoldingState(mapShape=mapShape, groupsOfFolds=groupsOfFolds, gap1ndex=gap1ndex, gap1ndexCeiling=gap1ndexCeiling, indexDimension=indexDimension, indexLeaf=indexLeaf, indexMiniGap=indexMiniGap, leaf1ndex=leaf1ndex, leafConnectee=leafConnectee, dimensionsUnconstrained=dimensionsUnconstrained, countDimensionsGapped=countDimensionsGapped, gapRangeStart=gapRangeStart, gapsWhere=gapsWhere, leafAbove=leafAbove, leafBelow=leafBelow, leafComparison=leafComparison)
    return state