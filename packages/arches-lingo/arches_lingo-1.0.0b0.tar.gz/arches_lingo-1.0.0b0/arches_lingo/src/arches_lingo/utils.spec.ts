import { ENGLISH } from "@/arches_lingo/constants.ts";
import {
    dataIsScheme,
    dataIsConcept,
    treeFromSchemes,
} from "@/arches_lingo/utils.ts";
import schemesFixture from "./fixtures/test_scheme.json";

import type { IconLabels, Scheme } from "@/arches_lingo/types";

const iconLabels: IconLabels = {
    concept: "Concept",
    scheme: "Scheme",
};

describe("Duck-typing helpers", () => {
    it("Should distinguish schemes from concepts", () => {
        const scheme = schemesFixture["schemes"][0];
        expect(dataIsScheme(scheme)).toBeTruthy();
        expect(dataIsConcept(scheme)).toBeFalsy();
    });
});

describe("Build scheme hierarchy", () => {
    it("Should shape schemes into TreeNodes", () => {
        const nodes = treeFromSchemes(
            schemesFixture["schemes"] as Scheme[],
            ENGLISH,
            ENGLISH,
            iconLabels,
            null,
        );
        const schemeNode = nodes[0];
        expect(schemeNode.label).toEqual("Test Scheme");
        expect(schemeNode.iconLabel).toEqual("Scheme");
        expect(schemeNode.data.top_concepts.length).toEqual(2);

        const topConcept = schemeNode.data.top_concepts[0];
        expect(topConcept.labels[0].value).toEqual("Concept 1");
        expect(topConcept.narrower.length).toEqual(4);
    });
    it("Should hide other top concepts when focusing child of another", () => {
        const nodesBeforeFocus = treeFromSchemes(
            schemesFixture["schemes"] as Scheme[],
            ENGLISH,
            ENGLISH,
            iconLabels,
            null,
        );
        const focusedNode = nodesBeforeFocus[0].children![0].children!.find(
            (n) => n.data.labels[0].value === "Concept 2",
        )!;
        const nodesAfterFocus = treeFromSchemes(
            schemesFixture["schemes"] as Scheme[],
            ENGLISH,
            ENGLISH,
            iconLabels,
            focusedNode,
        );
        const scheme = nodesAfterFocus[0];
        expect(scheme.children!.length).toEqual(1);
    });
});
