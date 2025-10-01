from collections.abc import Callable
from mapFolding.dataBaskets import (
	Array1DElephino, Array1DLeavesTotal, Array3DLeavesTotal, DatatypeElephino, DatatypeFoldsTotal, DatatypeLeavesTotal,
	MapFoldingState)

def unRePackDataclassA007822(callableTarget: Callable[[
	DatatypeFoldsTotal, DatatypeElephino, DatatypeElephino, DatatypeLeavesTotal, DatatypeLeavesTotal, DatatypeElephino,
	DatatypeLeavesTotal, DatatypeLeavesTotal, DatatypeLeavesTotal, Array1DLeavesTotal, Array1DElephino, Array1DLeavesTotal,
	Array1DLeavesTotal, Array1DLeavesTotal, Array1DLeavesTotal, Array3DLeavesTotal, DatatypeLeavesTotal, DatatypeLeavesTotal
], tuple[
	DatatypeFoldsTotal, DatatypeElephino, DatatypeElephino, DatatypeLeavesTotal, DatatypeLeavesTotal, DatatypeElephino,
	DatatypeLeavesTotal, DatatypeLeavesTotal, DatatypeLeavesTotal, Array1DLeavesTotal, Array1DElephino, Array1DLeavesTotal,
	Array1DLeavesTotal, Array1DLeavesTotal, Array1DLeavesTotal, Array3DLeavesTotal, DatatypeLeavesTotal, DatatypeLeavesTotal
]]) -> Callable[[MapFoldingState], MapFoldingState]:
	def workhorse(state: MapFoldingState) -> MapFoldingState:
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

		(groupsOfFolds, gap1ndex, gap1ndexCeiling, indexDimension, indexLeaf, indexMiniGap, leaf1ndex, leafConnectee, dimensionsUnconstrained,
		countDimensionsGapped, gapRangeStart, gapsWhere, leafAbove, leafBelow, leafComparison, connectionGraph, dimensionsTotal, leavesTotal
		) = callableTarget(
			groupsOfFolds, gap1ndex, gap1ndexCeiling, indexDimension, indexLeaf, indexMiniGap, leaf1ndex, leafConnectee, dimensionsUnconstrained,
			countDimensionsGapped, gapRangeStart, gapsWhere, leafAbove, leafBelow, leafComparison, connectionGraph, dimensionsTotal, leavesTotal)

		state = MapFoldingState(mapShape=mapShape, groupsOfFolds=groupsOfFolds, gap1ndex=gap1ndex, gap1ndexCeiling=gap1ndexCeiling,
			indexDimension=indexDimension, indexLeaf=indexLeaf, indexMiniGap=indexMiniGap, leaf1ndex=leaf1ndex, leafConnectee=leafConnectee,
			dimensionsUnconstrained=dimensionsUnconstrained, countDimensionsGapped=countDimensionsGapped, gapRangeStart=gapRangeStart,
			gapsWhere=gapsWhere, leafAbove=leafAbove, leafBelow=leafBelow, leafComparison=leafComparison)
		return state

	return workhorse

def unRePackDataclassAsynchronous(callableTarget: Callable[[
	DatatypeFoldsTotal, DatatypeElephino, DatatypeElephino, DatatypeLeavesTotal, DatatypeElephino,
	DatatypeLeavesTotal, DatatypeLeavesTotal, DatatypeLeavesTotal, Array1DLeavesTotal, Array1DElephino, Array1DLeavesTotal,
	Array1DLeavesTotal, Array1DLeavesTotal, Array3DLeavesTotal, DatatypeLeavesTotal, DatatypeLeavesTotal
], tuple[
	DatatypeFoldsTotal, DatatypeElephino, DatatypeElephino, DatatypeLeavesTotal, DatatypeElephino,
	DatatypeLeavesTotal, DatatypeLeavesTotal, DatatypeLeavesTotal, Array1DLeavesTotal, Array1DElephino, Array1DLeavesTotal,
	Array1DLeavesTotal, Array1DLeavesTotal, Array3DLeavesTotal, DatatypeLeavesTotal, DatatypeLeavesTotal
]]) -> Callable[[MapFoldingState], MapFoldingState]:
	def workhorse(state: MapFoldingState) -> MapFoldingState:
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

		(groupsOfFolds, gap1ndex, gap1ndexCeiling, indexDimension, indexMiniGap, leaf1ndex, leafConnectee, dimensionsUnconstrained,
		countDimensionsGapped, gapRangeStart, gapsWhere, leafAbove, leafBelow, connectionGraph, dimensionsTotal, leavesTotal
		) = callableTarget(
			groupsOfFolds, gap1ndex, gap1ndexCeiling, indexDimension, indexMiniGap, leaf1ndex, leafConnectee, dimensionsUnconstrained,
			countDimensionsGapped, gapRangeStart, gapsWhere, leafAbove, leafBelow, connectionGraph, dimensionsTotal, leavesTotal)

		state = MapFoldingState(mapShape=mapShape, groupsOfFolds=groupsOfFolds, gap1ndex=gap1ndex, gap1ndexCeiling=gap1ndexCeiling,
			indexDimension=indexDimension, indexLeaf=indexLeaf, indexMiniGap=indexMiniGap, leaf1ndex=leaf1ndex, leafConnectee=leafConnectee,
			dimensionsUnconstrained=dimensionsUnconstrained, countDimensionsGapped=countDimensionsGapped, gapRangeStart=gapRangeStart,
			gapsWhere=gapsWhere, leafAbove=leafAbove, leafBelow=leafBelow, leafComparison=leafComparison)
		return state

	return workhorse
