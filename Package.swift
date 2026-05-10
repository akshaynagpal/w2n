// swift-tools-version: 6.3

import PackageDescription

let package = Package(
  name: "w2ni18n",
  platforms: [.macOS(.v26),.visionOS(.v1),.iOS(.v16),.tvOS(.v16)],
  products: [
    // Products define the executables and libraries a package produces, making them visible to other packages.
    .library(
      name: "w2ni18n",
      targets: ["w2ni18n"]),
  ],
  dependencies: [
    .package(
      url: "https://github.com/bastie/JavApi4Swift.git",
      .upToNextMajor(from: "0.31.0")
    )
  ],
  targets: [
    // Targets are the basic building blocks of a package, defining a module or a test suite.
    // Targets can depend on other targets in this package and products from dependencies.
    .target(
      name: "w2ni18n",
      dependencies: [.product(name: "JavApi", package: "JavApi4Swift")],
      resources: [.process("Resources")]
    ),
    .testTarget(
      name: "w2ni18nTests",
      dependencies: ["w2ni18n"]
    ),
  ]
)

