AGGREGATE_FUNCTIONS = [
    "count",
    "min",
    "max",
    "sum",
    "avg",
    "any",
    "stddevPop",
    "stddevPopStable",
    "stddevSamp",
    "stddevSampStable",
    "varPop",
    "varSamp",
    "corr",
    "corr",
    "corrMatrix",
    "covarPop",
    "covarStable",
    "covarPopMatrix",
    "covarSamp",
    "covarSampStable",
    "covarSampMatrix",
    "entropy",
    "exponentialMovingAverage",
    "intervalLengthSum",
    "kolmogorovSmirnovTest",
    "mannwhitneyutest",
    "median",
    "rankCorr",
    "sumKahan",
    "studentTTest",
    "welchTTest",
    "analysisOfVariance",
    "any",
    "anyHeavy",
    "anyLast",
    "anyLast",
    "boundingRatio",
    "first_value",
    "last_value",
    "argMin",
    "argMax",
    "avgWeighted",
    "topK",
    "topKWeighted",
    "deltaSum",
    "deltaSumTimestamp",
    "flameGraph",
    "groupArray",
    "groupArrayLast",
    "groupUniqArray",
    "groupArrayInsertAt",
    "groupArrayMovingAvg",
    "groupArrayMovingSum",
    "groupArraySample",
    "groupArraySorted",
    "groupArrayIntersect",
    "groupBitAnd",
    "groupBitOr",
    "groupBitXor",
    "groupBitmap",
    "groupBitmapAnd",
    "groupBitmapOr",
    "groupBitmapXor",
    "sumWithOverflow",
    "sumMap",
    "sumMapWithOverflow",
    "sumMapFiltered",
    "sumMapFilteredWithOverflow",
    "minMap",
    "maxMap",
    "skewSamp",
    "skewPop",
    "kurtSamp",
    "kurtPop",
    "uniq",
    "uniqExact",
    "uniqCombined",
    "uniqCombined64",
    "uniqHLL12",
    "uniqTheta",
    "quantile",
    "quantiles",
    "quantileExact",
    "quantileExactLow",
    "quantileExactHigh",
    "quantileExactWeighted",
    "quantileTiming",
    "quantileTimingWeighted",
    "quantileDeterministic",
    "quantileTDigest",
    "quantileTDigestWeighted",
    "quantileBFloat16",
    "quantileBFloat16Weighted",
    "quantileDD",
    "simpleLinearRegression",
    "singleValueOrNull",
    "stochasticLinearRegression",
    "stochasticLogisticRegression",
    "categoricalInformationValue",
    "contingency",
    "cramersV",
    "cramersVBiasCorrected",
    "theilsU",
    "maxIntersections",
    "maxIntersectionsPosition",
    "meanZTest",
    "quantileGK",
    "quantileInterpolatedWeighted",
    "sparkBar",
    "sumCount",
    "largestTriangleThreeBuckets",
]

ARITHMETIC_FUNCTIONS = [
    "plus",
    "minus",
    "multiply",
    "divide",
    "intDiv",
    "intDivOrZero",
    "isFinite",
    "isInfinite",
    "ifNotFinite",
    "isNaN",
    "modulo",
    "moduloOrZero",
    "positiveModulo",
    "negate",
    "abs",
    "gcd",
    "lcm",
    "max2",
    "min2",
    "multiplyDecimal",
    "divideDecimal",
    "byteSwap"
]

ARRAY_FUNCTIONS = [
    "empty",
    "notEmpty",
    "length",
    "emptyArrayUInt8",
    "emptyArrayUInt16",
    "emptyArrayUInt32",
    "emptyArrayUInt64",
    "emptyArrayInt8",
    "emptyArrayInt16",
    "emptyArrayInt32",
    "emptyArrayInt64",
    "emptyArrayFloat32",
    "emptyArrayFloat64",
    "emptyArrayDate",
    "emptyArrayDateTime",
    "emptyArrayString",
    "emptyArrayToSingle",
    "range",
    "arrayWithConstant",
    "arrayConcat",
    "has",
    "hasAll",
    "hasAny",
    "hasSubstr",
    "indexOf",
    "arrayCount",
    "arrayDotProduct",
    "countEqual",
    "arrayEnumerate",
    "arrayEnumerateUniq",
    "arrayEnumerateUniqRanked",
    "arrayPopBack",
    "arrayPopFront",
    "arrayPushBack",
    "arrayPushFront",
    "arrayResize",
    "arraySlice",
    "arrayShingles",
    "arraySort",
    "arrayPartialSort",
    "arrayReverseSort",
    "arrayPartialReverseSort",
    "arrayShuffle",
    "arrayPartialShuffle",
    "arrayUniQ",
    "arrayJoin",
    "arrayDifference",
    "arrayDistinct",
    "arrayEnumerateDense",
    "arrayEnumerateDenseRanked",
    "arrayIntersect",
    "arrayJaccardIndex",
    "arrayReduce",
    "arrayReduceInRanges",
    "arrayFold",
    "arrayReverse",
    "reverse",
    "arrayFlatten",
    "arrayCompact",
    "arrayZip",
    "arrayAUC",
    "arrayMap",
    "arrayFilter",
    "arrayFill",
    "arrayReverseFill",
    "arraySplit",
    "arrayReverseSplit",
    "arrayExists",
    "arrayAll",
    "arrayFirst",
    "arrayFirstOrNull",
    "arrayLast",
    "arrayLastOrNull",
    "arrayFirstIndex",
    "arrayLastIndex",
    "arrayMin",
    "arrayMax",
    "arraySum",
    "arrayAvg",
    "arrayCumSum",
    "arrayCumSumNonNegative",
    "arrayProduct",
    "arrayRotateLeft",
    "arrayRotateRight",
    "arrayShiftLeft",
    "arrayShiftRight",
    "arrayRandomSample",
]

BIT_FUNCTIONS = [
    "bitAnd",
    "bitOr",
    "bitXor",
    "bitNot",
    "bitShiftLeft",
    "bitShiftRight",
    "bitRotateLeft",
    "bitRotateRight",
    "bitSlice",
    "byteSlice",
    "bitTest",
    "bitTestAll",
    "bitTestAny",
    "bitCount",
    "bitHammingDistance",
]

BITMAP_FUNCTIONS = [
    "bitmapBuild",
    "bitmapToArray",
    "bitmapSubsetInRange",
    "bitmapSubsetLimit",
    "subBitmap",
    "bitmapContains",
    "bitmapHasAny",
    "bitmapHasAll",
    "bitmapCardinality",
    "bitmapMin",
    "bitmapMax",
    "bitmapTransform",
    "bitmapAnd",
    "bitmapOr",
    "bitmapXor",
    "bitmapAndnot",
    "bitmapAndCardinality",
    "bitmapOrCardinality",
    "bitmapXorCardinality",
    "bitmapAndnotCardinality"
]

COMPARISON_FUNCTIONS = [
    "equals",
    "notEquals",
    "less",
    "greater",
    "lessOrEquals",
    "greaterOrEquals",
    "if",
    "multiIf",
    "greatest",
    "least",
    "clamp",
]

DATETIME_FUNCTIONS = [
    "makeDate",
    "makeDate32",
    "makeDateTime",
    "makeDateTime64",
    "timestamp",
    "timeZone",
    "serverTimeZone",
    "toTimeZone",
    "timeZoneOf",
    "timeZoneOffset",
    "toYear",
    "toQuarter",
    "toMonth",
    "toDayOfYear",
    "toDayOfMonth",
    "toDayOfWeek",
    "toHour",
    "toMinute",
    "toSecond",
    "toMillisecond",
    "toUnixTimestamp",
    "toStartOfYear",
    "toStartOfISOYear",
    "toStartOfQuarter",
    "toStartOfMonth",
    "toLastDayOfMonth",
    "toMonday",
    "toStartOfWeek",
    "toLastDayOfWeek",
    "toStartOfDay",
    "toStartOfHour",
    "toStartOfMinute",
    "toStartOfSecond",
    "toStartOfMillisecond",
    "toStartOfMicrosecond",
    "toStartOfNanosecond",
    "toStartOfFiveMinutes",
    "toStartOfTenMinutes",
    "toStartOfFifteenMinutes",
    "toStartOfInterval",
    "toTime",
    "toRelativeYearNum",
    "toRelativeQuarterNum",
    "toRelativeMonthNum",
    "toRelativeWeekNum",
    "toRelativeDayNum",
    "toRelativeHourNum",
    "toRelativeMinuteNum",
    "toRelativeSecondNum",
    "toISOYear",
    "toISOWeek",
    "toWeek",
    "toYearWeek",
    "toDaysSinceYearZero",
    "fromDaysSinceYearZero",
    "fromDaysSinceYearZero32",
    "age",
    "date_diff",
    "date_trunc",
    "date_add",
    "date_sub",
    "timestamp_add",
    "timestamp_sub",
    "addDate",
    "subDate",
    "now",
    "now64",
    "nowInBlock",
    "today",
    "yesterday",
    "timeSlot",
    "toYYYYMM",
    "toYYYYMMDD",
    "toYYYYMMDDhhmmss",
    "YYYYMMDDToDate",
    "YYYYMMDDToDate32",
    "YYYYMMDDhhmmssToDateTime",
    "YYYYMMDDhhmmssToDateTime64",
    "addYears",
    "addQuarters",
    "addMonths",
    "addWeeks",
    "addDays",
    "addHours",
    "addMinutes",
    "addSeconds",
    "addMilliseconds",
    "addMicroseconds",
    "addNanoseconds",
    "addInterval",
    "addTupleOfIntervals",
    "subtractYears",
    "subtractQuarters",
    "subtractMonths",
    "subtractWeeks",
    "subtractDays",
    "subtractHours",
    "subtractMinutes",
    "subtractSeconds",
    "subtractMilliseconds",
    "subtractMicroseconds",
    "subtractNanoseconds",
    "subtractInterval",
    "subtractTupleOfIntervals",
    "timeSlots",
    "formatDateTime",
    "formatDateTimeInJodaSyntax",
    "dateName",
    "monthName",
    "fromUnixTimestamp",
    "fromUnixTimestampInJodaSyntax",
    "toModifiedJulianDay",
    "toModifiedJulianDayOrNull",
    "fromModifiedJulianDay",
    "fromModifiedJulianDayOrNull",
    "toUTCTimestamp",
    "fromUTCTimestamp",
    "UTCTimestamp",
    "timeDiff"
]

DICT_FUNCTIONS = [
    "dictGet",
    "dictGetOrDefault",
    "dictGetOrNull",
    "dictHas",
    "dictGetHierarchy",
    "dictIsIn",
    "dictGetChildren",
    "dictGetDescendant",
    "dictGetAll",
    "dictGetInt8",
    "dictGetInt16",
    "dictGetInt32",
    "dictGetInt64",
    "dictGetUInt8",
    "dictGetUInt16",
    "dictGetUInt32",
    "dictGetUInt64",
    "dictGetFloat32",
    "dictGetFloat64",
    "dictGetDate",
    "dictGetDateTime",
    "dictGetUUID",
    "dictGetString",
    "dictGetIPv4",
    "dictGetIPv6",
    "regionToName",
    "regionToCity",
    "regionToArea",
    "regionToDistrict",
    "regionToCountry",
    "regionToContinent",
    "regionToTopContinent",
    "regionToPopulation",
    "regionIn",
    "regionHierarchy",
]

DISTANCE_FUNCTIONS = [
    "L1Norm",
    "L2Norm",
    "L2SquaredNorm",
    "LinfNorm",
    "LpNorm",
    "L1Distance",
    "L2Distance",
    "L2SquaredDistance",
    "LinfDistance",
    "LpDistance",
    "L1Normalize",
    "L2Normalize",
    "LinfNormalize",
    "LpNormalize",
    "cosineDistance",
]

GEOGRAPHY_FUNCTIONS = [
    "greatCircleDistance",
    "geoDistance",
    "greatCircleAngle",
    "pointInEllipses",
    "pointInPolygon",
    "geohashEncode",
    "geohashDecode",
    "geohashesInBox",
    "h3IsValid",
    "h3GetResolution",
    "h3EdgeAngle",
    "h3EdgeLengthM",
    "h3EdgeLengthKm",
    "geoToH3",
    "h3ToGeo",
    "h3ToGeoBoundary",
    "h3kRing",
    "h3GetBaseCell",
    "h3HexAreaM2",
    "h3HexAreaKm2",
    "h3IndexesAreNeighbors",
    "h3ToChildren",
    "h3ToParent",
    "h3ToString",
    "stringToH3",
    "h3GetResolution",
    "h3IsResClassIII",
    "h3IsPentagon",
    "h3GetFaces",
    "h3CellAreaM2",
    "h3CellAreaRads2",
    "h3ToCenterChild",
    "h3ExactEdgeLengthM",
    "h3ExactEdgeLengthKm",
    "h3ExactEdgeLengthRads",
    "h3NumHexagons",
    "h3Line",
    "h3Distance",
    "h3HexRing",
    "h3GetUnidirectionalEdge",
    "h3UnidirectionalEdgeIsValid",
    "h3GetOriginIndexFromUnidirectionalEdge",
    "h3GetDestinationIndexFromUnidirectionalEdge",
    "h3GetIndexesFromUnidirectionalEdge",
    "h3GetUnidirectionalEdgesFromHexagon",
    "h3GetUnidirectionalEdgeBoundary",
    "geoToS2",
    "s2ToGeo",
    "s2GetNeighbors",
    "s2CellsIntersect",
    "s2CapContains",
    "s2CapUnion",
    "s2RectAdd",
    "s2RectContains",
    "s2RectUnion",
    "s2RectIntersection",
    "SVG"
]

ENCODE_FUNCTIONS = [
    "char",
    "hex",
    "unhex",
    "bin",
    "unbin",
    "bitmaskToList",
    "bitmaskToArray",
    "bitPositionsToArray",
    "mortonEncode",
    "mortonDecode",
    "hilbertEncode",
    "hilbertDecode",
]

ENCRYPTION_FUNCTIONS = [
    "encrypt",
    "aes_encrypt_mysql",
    "decrypt",
    "tryDecrypt",
    "aes_decrypt_mysql",
]

FILE_FUNCTIONS = [
    "file",
]

HASH_FUNCTIONS = [
    "halfMD5",
    "MD4",
    "MD5",
    "sipHash64",
    "sipHash64Keyed",
    "sipHash128",
    "sipHash128Keyed",
    "sipHash128Reference",
    "sipHash128ReferenceKeyed",
    "cityHash64",
    "intHash32",
    "intHash64",
    "SHA1",
    "SHA224",
    "SHA256",
    "SHA512",
    "SHA512_256",
    "BLAKE3",
    "URLHash",
    "farmFingerprint64",
    "farmHash64",
    "javaHash",
    "javaHashUTF16LE",
    "hiveHash",
    "metroHash64",
    "jumpConsistentHash",
    "kostikConsistentHash",
    "murmurHash2_32",
    "murmurHash2_64",
    "gccMurmurHash",
    "kafkaMurmurHash",
    "murmurHash3_32",
    "murmurHash3_64",
    "murmurHash3_128",
    "xxh3",
    "xxHash32",
    "xxHash64",
    "ngramSimHash",
    "ngramSimHashCaseInsensitive",
    "ngramSimHashUTF8",
    "ngramSimHashCaseInsensitiveUTF8",
    "wordShingleSimHash",
    "wordShingleSimHashCaseInsensitive",
    "wordShingleSimHashUTF8",
    "wordShingleSimHashCaseInsensitiveUTF8",
    "wyHash64",
    "ngramMinHash",
    "ngramMinHashCaseInsensitive",
    "ngramMinHashUTF8",
    "ngramMinHashCaseInsensitiveUTF8",
    "ngramMinHashArg",
    "ngramMinHashArgCaseInsensitive",
    "ngramMinHashArgUTF8",
    "ngramMinHashArgCaseInsensitiveUTF8",
    "wordShingleMinHash",
    "wordShingleMinHashCaseInsensitive",
    "wordShingleMinHashUTF8",
    "wordShingleMinHashCaseInsensitiveUTF8",
    "wordShingleMinHashArg",
    "wordShingleMinHashArgCaseInsensitive",
    "wordShingleMinHashArgUTF8",
    "wordShingleMinHashArgCaseInsensitiveUTF8",
    "sqidEncode",
    "sqidDecode",
]

IP_FUNCTIONS = [
    "IPv4NumToString",
    "IPv4StringToNum",
    "IPv4StringToNumOrDefault",
    "IPv4StringToNumOrNull",
    "IPv4NumToStringClassC",
    "IPv6NumToString",
    "IPv6StringToNum",
    "IPv6StringToNumOrDefault",
    "IPv6StringToNumOrNull",
    "IPv4ToIPv6",
    "cutIPv6",
    "IPv4CIDRToRange",
    "IPv6CIDRToRange",
    "toIPv4",
    "toIPv4OrDefault",
    "toIPv4OrNull",
    "toIPv6OrDefault",
    "toIPv6OrNull",
    "toIPv6",
    "IPv6StringToNumOrDefault",
    "IPv6StringToNumOrNull",
    "isIPv4String",
    "isIPv6String",
    "isIPAddressInRange",
]

JSON_FUNCTIONS = [
    "simpleJSONHas",
    "simpleJSONExtractUInt",
    "simpleJSONExtractInt",
    "simpleJSONExtractFloat",
    "simpleJSONExtractBool",
    "simpleJSONExtractRaw",
    "simpleJSONExtractString",
    "isValidJSON",
    "JSONHas",
    "JSONLength",
    "JSONType",
    "JSONExtractUInt",
    "JSONExtractInt",
    "JSONExtractFloat",
    "JSONExtractBool",
    "JSONExtractString",
    "JSONExtract",
    "JSONExtractKeysAndValues",
    "JSONExtractKeys",
    "JSONExtractRaw",
    "JSONExtractArrayRaw",
    "JSONExtractKeysAndValuesRaw",
    "JSON_EXISTS",
    "JSON_QUERY",
    "JSON_VALUE",
    "toJSONString",
    "JSONArrayLength",
    "jsonMergePatch",
]

LOGICAL_FUNCTIONS = [
    "and",
    "or",
    "not",
    "xor",
]

MAP_FUNCTIONS = [
    "map",
    "mapFromArrays",
    "extractKeyValuePairs",
    "extractKeyValuePairsWithEscaping",
    "mapAdd",
    "mapSubtract",
    "mapPopulateSeries",
    "mapContains",
    "mapKeys",
    "mapValues",
    "mapContainsKeyLike",
    "mapExtractKeyLike",
    "mapApply",
    "mapFilter",
    "mapUpdate",
    "mapConcat",
    "mapExists",
    "mapAll",
    "mapSort",
    "mapReverseSort",
]

MATH_FUNCTIONS = [
    "e",
    "pi",
    "exp",
    "log",
    "exp2",
    "intExp2",
    "log2",
    "exp10",
    "intExp10",
    "log10",
    "sqrt",
    "cbrt",
    "erf",
    "erfc",
    "lgamma",
    "tgamma",
    "sin",
    "cos",
    "tan",
    "asin",
    "acos",
    "atan",
    "pow",
    "cosh",
    "acosh",
    "sinh",
    "asinh",
    "tanh",
    "atanh",
    "atan2",
    "hypot",
    "log1p",
    "sign",
    "sigmoid",
    "degrees",
    "radians",
    "factorial",
    "width_bucket",
    "proportionsZTest",
    "floor",
    "ceiling",
    "truncate",
    "round",
    "roundBankers",
    "roundToExp2",
    "roundDuration",
    "roundAge",
    "roundDown"
]

NLP_FUNCTIONS = [
    "stem",
    "lemmatize",
    "synonyms",
    "detectLanguage",
    "detectLanguageMixed",
    "detectLanguageUnknown",
    "detectCharset",
]

NULLABLE_FUNCTIONS = [
    "isNull",
    "isNullable",
    "isNotNull",
    "isNotDistinctFrom",
    "isZeroOrNull",
    "coalesce",
    "ifNull",
    "nullIf",
    "assumeNotNull",
    "toNullable",
]

OTHER_FUNCTIONS = [
    "hostName",
    "getMacro",
    "FQDN",
    "basename",
    "visibleWidth",
    "toTypeName",
    "blockSize",
    "byteSize",
    "materialize",
    "ignore",
    "sleep",
    "sleepEachRow",
    "currentDatabase",
    "currentUser",
    "isConstant",
    "hasColumnInTable",
    "hasThreadFuzzer",
    "bar",
    "transform",
    "formatReadableDecimalSize",
    "formatReadableSize",
    "formatReadableQuantity",
    "formatReadableTimeDelta",
    "parseReadableSize",
    "parseReadableSizeOrNull",
    "parseReadableSizeOrZero",
    "parseTimeDelta",
    "least",
    "greatest",
    "uptime",
    "version",
    "buildId",
    "blockNumber",
    "rowNumberInBlock",
    "rowNumberInAllBlocks",
    "neighbor",
    "runningDifference",
    "runningDifferenceStartingWithFirstValue",
    "runningConcurrency",
    "MACNumToString",
    "MACStringToNum",
    "MACStringToOUI",
    "getSizeOfEnumType",
    "blockSerializedSize",
    "toColumnTypeName",
    "dumpColumnStructure",
    "defaultValueOfArgumentType",
    "defaultValueOfTypeName",
    "indexHint",
    "replicate",
    "revision",
    "filesystemAvailable",
    "filesystemFree",
    "filesystemCapacity",
    "initializeAggregation",
    "finalizeAggregation",
    "runningAccumulate",
    "joinGet",
    "catboostEvaluate",
    "throwIf",
    "identity",
    "getSetting",
    "isDecimalOverflow",
    "countDigits",
    "errorCodeToName",
    "tcpPort",
    "currentProfiles",
    "enabledProfiles",
    "defaultProfiles",
    "currentRoles",
    "enabledRoles",
    "defaultRoles",
    "getServerPort",
    "queryID",
    "initialQueryID",
    "shardNum",
    "shardCount",
    "getOSKernelVersion",
    "zookeeperSessionUptime",
    "generateRandomStructure",
    "structureToCapnProtoSchema",
    "structureToProtobufSchema",
    "formatQuery",
    "formatQuerySingleLine",
    "variantElement",
    "variantType",
    "minSampleSizeConversion",
    "minSampleSizeContinuous",
    "connectionId",
    "connection_id",
    "getClientHTTPHeader",
    "showCertificate",
    "lowCardinalityIndices",
    "lowCardinalityKeys",
]

RANDOM_FUNCTIONS = [
    "rand",
    "rand64",
    "randCanonical",
    "randConstant",
    "randUniform",
    "randNormal",
    "randLogNormal",
    "randBinomial",
    "randNegativeBinomial",
    "randPoisson",
    "randBernoulli",
    "randExponential",
    "randChiSquared",
    "randStudentT",
    "randFisherF",
    "randomString",
    "randomFixedString",
    "randomPrintableASCII",
    "randomStringUTF8",
    "fuzzBits",
]

STRING_FUNCTIONS = [
    "empty",
    "notEmpty",
    "length",
    "lengthUTF8",
    "left",
    "leftUTF8",
    "leftPad",
    "leftPadUTF8",
    "right",
    "rightUTF8",
    "rightPad",
    "rightPadUTF8",
    "lower",
    "upper",
    "lowerUTF8",
    "upperUTF8",
    "isValidUTF8",
    "toValidUTF8",
    "repeat",
    "space",
    "reverse",
    "reverseUTF8",
    "concat",
    "concatAssumeInjective",
    "concatWithSeparator",
    "concatWithSeparatorAssumeInjective",
    "substring",
    "substringUTF8",
    "substringIndex",
    "substringIndexUTF8",
    "appendTrailingCharIfAbsent",
    "convertCharset",
    "base58Encode",
    "base58Decode",
    "tryBase58Decode",
    "base64Encode",
    "base64UrlEncode",
    "base64Decode",
    "base64UrlDecode",
    "tryBase64Decode",
    "tryBase64UrlDecode",
    "endsWith",
    "endsWithUTF8",
    "startsWith",
    "startsWithUTF8",
    "trim",
    "trimLeft",
    "trimRight",
    "trimBoth",
    "CRC32",
    "CRC32IEEE",
    "CRC64",
    "normalizeQuery",
    "normalizedQueryHash",
    "normalizeUTF8NFC",
    "normalizeUTF8NFD",
    "normalizeUTF8NFKC",
    "normalizeUTF8NFKD",
    "encodeXMLComponent",
    "decodeXMLComponent",
    "decodeHTMLComponent",
    "extractTextFromHTML",
    "ascii",
    "soundex",
    "punycodeEncode",
    "punycodeDecode",
    "tryPunycodeDecode",
    "idnaEncode",
    "tryIdnaEncode",
    "idnaDecode",
    "byteHammingDistance",
    "stringJaccardIndex",
    "stringJaccardIndexUTF8",
    "editDistance",
    "damerauLevenshteinDistance",
    "jaroSimilarity",
    "jaroWinklerSimilarity",
    "initcap",
    "initcapUTF8",
    "firstLine",
    "splitByChar",
    "splitByString",
    "splitByRegexp",
    "splitByWhitespace",
    "splitByNonAlpha",
    "arrayStringConcat",
    "alphaTokens",
    "extractAllGroups",
    "ngrams",
    "tokens",
    "position",
    "locate",
    "positionCaseInsensitive",
    "positionUTF8",
    "positionCaseInsensitiveUTF8",
    "multiSearchAllPositions",
    "multiSearchAllPositionsCaseInsensitive",
    "multiSearchAllPositionsUTF8",
    "multiSearchAllPositionsCaseInsensitiveUTF8",
    "multiSearchFirstPosition",
    "multiSearchFirstPositionCaseInsensitive",
    "multiSearchFirstPositionUTF8",
    "multiSearchFirstPositionCaseInsensitiveUTF8",
    "multiSearchFirstIndex",
    "multiSearchFirstIndexCaseInsensitive",
    "multiSearchFirstIndexUTF8",
    "multiSearchFirstIndexCaseInsensitiveUTF8",
    "multiSearchAny",
    "multiSearchAnyCaseInsensitive",
    "multiSearchAnyUTF8",
    "multiSearchAnyCaseInsensitiveUTF8",
    "match",
    "multiMatchAny",
    "multiMatchAnyIndex",
    "multiMatchAllIndices",
    "multiFuzzyMatchAny",
    "multiFuzzyMatchAnyIndex",
    "multiFuzzyMatchAllIndices",
    "extract",
    "extractAll",
    "replaceOne",
    "replaceAll",
    "replaceRegexpOne",
    "replaceRegexpAll",
    "regexpQuoteMeta",
    "format",
    "translate",
    "translateUTF8",
]

TIME_SERIES_FUNCTIONS = [
    "seriesOutliersDetectTukey",
    "seriesPeriodDetectFFT",
    "seriesDecomposeSTL"
]

TIME_WINDOW_FUNCTIONS = [
    "tumble",
    "hop",
    "tumbleStart",
    "tumbleEnd",
    "hopStart",
    "hopEnd",
]

TUPLE_FUNCTIONS = [
    "tuple",
    "tupleElement",
    "untuple",
    "tupleHammingDistance",
    "tupleToNameValuePairs",
    "tuplePlus",
    "tupleMinus",
    "tupleMultiply",
    "tupleDivide",
    "tupleNegate",
    "tupleMultiplyByNumber",
    "tupleDivideByNumber",
    "tupleConcat",
    "tupleIntDiv",
    "tupleIntDivOrZero",
    "tupleIntDivByNumber",
    "tupleIntDivOrZeroByNumber",
    "tupleModulo",
    "tupleModuloByNumber",
    "flattenTuple",
]

TYPE_CONVERSION_FUNCTIONS = [
    "toInt8",
    "toInt16",
    "toInt32",
    "toInt64",
    "toInt128",
    "toInt256",
    "toInt8OrZero",
    "toInt16OrZero",
    "toInt32OrZero",
    "toInt64OrZero",
    "toInt128OrZero",
    "toInt256OrZero",
    "toInt8OrNull",
    "toInt16OrNull",
    "toInt32OrNull",
    "toInt64OrNull",
    "toInt128OrNull",
    "toInt256OrNull",
    "toInt8OrDefault",
    "toInt16OrDefault",
    "toInt32OrDefault",
    "toInt64OrDefault",
    "toInt128OrDefault",
    "toInt256OrDefault",
    "toUInt8",
    "toUInt16",
    "toUInt32",
    "toUInt64",
    "toUInt128",
    "toUInt256",
    "toUInt8OrZero",
    "toUInt16OrZero",
    "toUInt32OrZero",
    "toUInt64OrZero",
    "toUInt128OrZero",
    "toUInt256OrZero",
    "toUInt8OrNull",
    "toUInt16OrNull",
    "toUInt32OrNull",
    "toUInt64OrNull",
    "toUInt128OrNull",
    "toUInt256OrNull",
    "toUInt8OrDefault",
    "toUInt16OrDefault",
    "toUInt32OrDefault",
    "toUInt64OrDefault",
    "toUInt128OrDefault",
    "toUInt256OrDefault",
    "toFloat32",
    "toFloat64",
    "toFloat32OrZero",
    "toFloat64OrZero",
    "toFloat32OrNull",
    "toFloat64OrNull",
    "toFloat32OrDefault",
    "toFloat64OrDefault",
    "toDate",
    "toDateOrZero",
    "toDateOrNull",
    "toDateOrDefault",
    "toDateTime",
    "toDateTimeOrZero",
    "toDateTimeOrNull",
    "toDateTimeOrDefault",
    "toDate32",
    "toDate32OrZero",
    "toDate32OrNull",
    "toDate32OrDefault",
    "toDateTime64",
    "toDateTime64OrZero",
    "toDateTime64OrNull",
    "toDateTime64OrDefault",
    "toDecimal32",
    "toDecimal64",
    "toDecimal128",
    "toDecimal256",
    "toDecimal32OrNull",
    "toDecimal64OrNull",
    "toDecimal128OrNull",
    "toDecimal256OrNull",
    "toDecimal32OrDefault",
    "toDecimal64OrDefault",
    "toDecimal128OrDefault",
    "toDecimal256OrDefault",
    "toDecimal32OrZero",
    "toDecimal64OrZero",
    "toDecimal128OrZero",
    "toDecimal256OrZero",
    "toString",
    "toFixedString",
    "toStringCutToZero",
    "toDecimalString",
    "reinterpretAsUInt8",
    "reinterpretAsUInt16",
    "reinterpretAsUInt32",
    "reinterpretAsUInt64",
    "reinterpretAsUInt128",
    "reinterpretAsUInt256",
    "reinterpretAsInt8",
    "reinterpretAsInt16",
    "reinterpretAsInt32",
    "reinterpretAsInt64",
    "reinterpretAsInt128",
    "reinterpretAsInt256",
    "reinterpretAsFloat32",
    "reinterpretAsFloat64",
    "reinterpretAsDate",
    "reinterpretAsDateTime",
    "reinterpretAsString",
    "reinterpretAsFixedString",
    "reinterpretAsUUID",
    "reinterpret",
    "CAST",
    "accurateCast",
    "accurateCastOrNull",
    "accurateCastOrDefault",
    "toIntervalYear",
    "toIntervalQuarter",
    "toIntervalMonth",
    "toIntervalWeek",
    "toIntervalDay",
    "toIntervalHour",
    "toIntervalMinute",
    "toIntervalSecond",
    "parseDateTime",
    "parseDateTimeOrZero",
    "parseDateTimeOrNull",
    "parseDateTimeInJodaSyntax",
    "parseDateTimeInJodaSyntaxOrZero",
    "parseDateTimeInJodaSyntaxOrNull",
    "parseDateTimeBestEffort",
    "parseDateTime32BestEffort",
    "parseDateTimeBestEffortUS",
    "parseDateTimeBestEffortOrNull",
    "parseDateTime32BestEffortOrNull",
    "parseDateTimeBestEffortOrZero",
    "parseDateTime32BestEffortOrZero",
    "parseDateTimeBestEffortUSOrNull",
    "parseDateTimeBestEffortUSOrZero",
    "parseDateTime64BestEffort",
    "parseDateTime64BestEffortUS",
    "parseDateTime64BestEffortOrNull",
    "parseDateTime64BestEffortOrZero",
    "parseDateTime64BestEffortUSOrNull",
    "parseDateTime64BestEffortUSOrZero",
    "toLowCardinality",
    "toUnixTimestamp64Milli",
    "toUnixTimestamp64Micro",
    "toUnixTimestamp64Nano",
    "fromUnixTimestamp64Milli",
    "fromUnixTimestamp64Micro",
    "fromUnixTimestamp64Nano",
    "formatRow",
    "formatRowNoNewline",
]

URL_FUNCTIONS = [
    "protocol",
    "domain",
    "domainRFC",
    "domainWithoutWWW",
    "domainWithoutWWWRFC",
    "topLevelDomain",
    "topLevelDomainRFC",
    "firstSignificantSubdomain",
    "firstSignificantSubdomainRFC",
    "cutToFirstSignificantSubdomain",
    "cutToFirstSignificantSubdomainRFC",
    "cutToFirstSignificantSubdomainWithWWW",
    "cutToFirstSignificantSubdomainWithWWWRFC",
    "cutToFirstSignificantSubdomainCustom",
    "cutToFirstSignificantSubdomainCustomRFC",
    "cutToFirstSignificantSubdomainCustomWithWWW",
    "cutToFirstSignificantSubdomainCustomWithWWWRFC",
    "firstSignificantSubdomainCustom",
    "firstSignificantSubdomainCustomRFC",
    "port",
    "portRFC",
    "path",
    "pathFull",
    "queryString",
    "fragment",
    "queryStringAndFragment",
    "extractURLParameter",
    "extractURLParameters",
    "extractURLParameterNames",
    "URLHierarchy",
    "URLPathHierarchy",
    "encodeURLComponent",
    "decodeURLComponent",
    "encodeURLFormComponent",
    "decodeURLFormComponent",
    "netloc",
    "cutWWW",
    "cutQueryString",
    "cutFragment",
    "cutQueryStringAndFragment",
    "cutURLParameter",
]

UUID_FUNCTIONS = [
    "generateUUIDv4",
    "generateUUIDv7",
    "empty",
    "notEmpty",
    "toUUID",
    "toUUIDOrDefault",
    "toUUIDOrNull",
    "toUUIDOrZero",
    "UUIDStringToNum",
    "UUIDNumToString",
    "UUIDToNum",
    "UUIDv7ToDateTime",
    "serverUUID",
    "generateSnowflakeID",
    "snowflakeToDateTime",
    "snowflakeToDateTime64",
    "dateTimeToSnowflake",
    "dateTime64ToSnowflake",
    "generateULID",
    "ULIDStringToDateTime"
]

UNIQTHETA_FUNCTIONS = [
    "uniqThetaUnion",
    "uniqThetaIntersect",
    "uniqThetaNot",
]
